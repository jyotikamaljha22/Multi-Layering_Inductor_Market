import os
import csv
import base64
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Strategic Market Research | TDK Corporation Boardroom",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded", 
)

# =========================
# GLOBAL THEME & PALETTE
# =========================
BURGUNDY = "#4A0C25" 
BURGUNDY_DARK = "#2D0716"
BURGUNDY_MID = "#7A143D"
GOLD = "#C49A23"
INK = "#1A1A1A"
MUTED = "#6B7280"
BORDER_COLOR = "#E5E7EB" # Fixed the previous NameError by explicitly naming this

PREVIEW_NOTE = "SMR Confidential. High-resolution unit-level projections and competitive cost curves are restricted to full report holders."

@st.cache_data
def load_logo_base64() -> str | None:
    candidates = [Path("smrlogonew.svg"), Path(__file__).with_name("smrlogonew.svg"), Path.cwd() / "smrlogonew.svg"]
    for path in candidates:
        if path.exists():
            try: return base64.b64encode(path.read_bytes()).decode("utf-8")
            except Exception: pass
    return None

LOGO_B64 = load_logo_base64()

# =========================
# CSS & UI POLISH
# =========================
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{ font-family: 'Plus Jakarta Sans', sans-serif !important; color: {INK} !important; }}
    [data-testid="stToolbar"] {{ display: none !important; }}
    footer {{ display: none !important; }}
    header[data-testid="stHeader"] {{ background: transparent !important; box-shadow: none !important; }}

    /* PERMANENT SIDEBAR LOCK */
    [data-testid="stSidebarCollapseButton"] {{ display: none !important; width: 0 !important; }}
    [data-testid="stSidebar"] {{ background: {BURGUNDY_DARK} !important; border-right: 1px solid rgba(255,255,255,0.05) !important; }}
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {{ color: rgba(255,255,255,0.9) !important; }}

    /* INPUT FIELDS & FORMS */
    .stTextInput input {{
        border-radius: 8px !important; border: 1px solid #E5E7EB !important;
        padding: 12px 14px !important; background-color: #ffffff !important; color: #1A1A1A !important;
    }}
    .stButton > button {{
        background: linear-gradient(135deg, {GOLD} 0%, #A37F1C 100%) !important;
        color: {BURGUNDY_DARK} !important; border: none !important; border-radius: 8px !important;
        padding: 10px 24px !important; font-weight: 800 !important; box-shadow: 0 4px 12px rgba(196,154,35,0.3) !important;
    }}

    /* NAV LINKS */
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] {{
        padding: 6px 12px !important; margin-bottom: 1px !important; border-radius: 6px !important;
    }}
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[checked]) {{
         background: rgba(255,255,255,0.1) !important; border-left: 4px solid {GOLD} !important;
    }}
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] p {{ color: white !important; font-size: 0.82rem !important; font-weight: 600 !important; }}

    /* HERO & CARDS */
    .hero {{
      background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_MID} 100%);
      color: white; border-radius: 12px; padding: 30px 40px; margin-bottom: 24px; position: relative; overflow: hidden;
    }}
    .metric-card {{
      background: white; border: 1px solid #E5E7EB; border-radius: 10px; padding: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.02); transition: all 0.3s ease;
    }}
    .metric-label {{ color: {MUTED}; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px; }}
    .metric-value {{ color: {BURGUNDY}; font-size: 2rem; font-weight: 800; line-height: 1; }}
    
    .insight-box {{
      background: #ffffff; border-left: 5px solid {GOLD}; border-radius: 6px; padding: 16px 20px;
      margin-bottom: 20px; box-shadow: 0 4px 12px rgba(196,154,35,0.05); font-size: 0.9rem;
    }}
    
    /* TEASER BLUR EFFECT */
    .locked-overlay {{
        background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 80%);
        padding: 30px; text-align: center; border-radius: 0 0 10px 10px; margin-top: -50px; position: relative; z-index: 10;
    }}
    .blurred {{ filter: blur(5px); opacity: 0.3; pointer-events: none; user-select: none; }}
    
    .viewer-chip {{
      display:inline-block; padding:4px 12px; border-radius:999px; font-size:0.7rem; font-weight:700;
      background: rgba(255,255,255,0.1); color: {GOLD}; margin-top:5px; margin-bottom: 10px;
      border: 1px solid rgba(255,255,255,0.15);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- JAILBREAK SCRIPT ---
components.html(
    """<script>setTimeout(function() {var e = window.parent.document.querySelector('[data-testid="collapsedControl"]'); if(e) e.click();}, 100);</script>""",
    height=0, width=0
)

# =========================
# CORE UI FUNCTIONS
# =========================
def brand_sidebar():
    logo_html = f'<img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:40px; width:auto; margin-bottom:10px; filter: brightness(0) invert(1);" />' if LOGO_B64 else ""
    st.sidebar.markdown(f'<div class="smr-brand">{logo_html}<h1 style="color:white; margin:0; font-size:1rem; font-weight:800; letter-spacing:-0.02em; line-height:1.2;">Strategic Market Research</h1><p style="color:rgba(255,255,255,0.6); margin:4px 0 0 0; font-size:0.75rem; font-weight:500;">Global Multilayer Inductor<br>Executive Boardroom</p></div>', unsafe_allow_html=True)

def card_metric(label: str, value: str, foot: str):
    st.markdown(f'<div class="metric-card"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div style="color:{MUTED}; font-size:0.75rem; margin-top:6px;">{foot}</div></div>', unsafe_allow_html=True)

def chart_theme(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=INK, family="Plus Jakarta Sans"),
        margin=dict(l=10, r=10, t=40, b=10), legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="rgba(0,0,0,0.05)", zeroline=False)
    return fig

def render_teaser_lock(text="Granular Unit-Level Data Unlocked with Report Purchase."):
    st.markdown(f"""
    <div class="locked-overlay">
        <p style="color:{BURGUNDY}; font-weight:800; font-size:1rem;">🔒 ACCESS RESTRICTED</p>
        <p style="color:{MUTED}; font-size:0.8rem; margin-bottom:12px;">{text}</p>
        <button style="background:{BURGUNDY}; color:white; border:none; padding:6px 16px; border-radius:4px; font-weight:700; cursor:pointer; font-size:0.8rem;">Request Access</button>
    </div>
    """, unsafe_allow_html=True)

# =========================
# DATA ENGINE (20-CHAPTER MAPPING)
# =========================
@st.cache_data
def load_data():
    d = {}
    # Revenue (Chapters 1 & 2)
    d["rev_vol"] = pd.DataFrame({
        "Year": ["2025", "2027", "2029", "2031", "2033", "2035"],
        "Revenue ($Mn)": [1446.7, 1555.2, 1678.9, 1810.1, 1955.4, 2115.3],
        "Units (Bn)": [77.0, 83.6, 90.9, 98.8, 107.4, 116.1]
    })
    # Pricing (Chapter 3)
    d["pricing"] = pd.DataFrame({
        "Segment": ["Automotive-Qualified", "RF / High-Freq", "Compact Ferrite"],
        "2025 ASP ($)": [0.0360, 0.0220, 0.0135],
        "2035 ASP ($)": [0.0380, 0.0210, 0.0125]
    })
    # Devices (Chapters 4-6)
    d["devices"] = pd.DataFrame({
        "Category": ["Smartphones", "Wearables (TWS)", "Electric Vehicles (EV)", "IoT Edge Modules"],
        "2025 Bn units": [49.6, 4.3, 3.5, 12.2],
        "2035 Bn units": [60.8, 7.5, 10.5, 27.0]
    })
    # Applications (Chapter 7)
    d["apps"] = pd.DataFrame({
        "App": ["RF Front-End", "Power/Filter/NFC", "Auto PoC Networks"],
        "Share 2025 (%)": [58.0, 32.8, 9.2],
        "Share 2035 (%)": [54.1, 31.8, 14.1]
    })
    # Miniaturization (Chapter 8)
    d["mini"] = pd.DataFrame({
        "Year": ["2025", "2030", "2035"],
        "Standard (0402+)": [40, 25, 10],
        "Precision (0201)": [50, 55, 45],
        "Elite (01005)": [10, 20, 45]
    })
    # Regional (Chapters 9-11)
    d["regions"] = pd.DataFrame({
        "Region": ["China", "India", "USA", "Germany", "Japan", "Vietnam/ASEAN"],
        "2035 Rev ($Mn)": [559.9, 253.3, 214.8, 65.8, 73.0, 48.4],
        "MapCode": ["CHN", "IND", "USA", "DEU", "JPN", "VNM"]
    })
    # Competition (Chapters 12-14)
    d["comp"] = pd.DataFrame({
        "Company": ["Murata", "TDK (Client)", "Samsung EM", "Taiyo Yuden", "Sunlord", "YAGEO"],
        "2025 Share (%)": [31, 22, 9, 8, 7, 6]
    })
    # Tariffs (Chapter 17)
    d["tariffs"] = pd.DataFrame({
        "Geography": ["United States", "Germany", "Japan", "China", "Vietnam"],
        "Combined Multiplier": [1.188, 1.145, 1.134, 0.969, 0.836]
    })
    return d

# =========================
# PAGE RENDERERS
# =========================
def render_market_core(data):
    st.markdown('<div class="hero"><h2>Pillar 1: Market Core & Sizing</h2><p>Chapters 1-2: Global Size, Volume Trajectories, and the Decoupling Analysis.</p></div>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: card_metric("Total TAM 2035", "$2.12 Bn", "Base-case revenue projection.")
    with c2: card_metric("Unit Volume", "116.1 Bn", "Projected component load.")
    with c3: card_metric("Market CAGR", "3.87%", "Steady compounding expansion.")
    with c4: card_metric("Auto Penetration", "14.2%", "Highest growth value segment.")

    st.markdown("""<div class="insight-box"><strong>Boardroom Insight:</strong> While unit volume grows at a 4.19% CAGR, revenue lags at 3.87% due to systemic price deflation in consumer segments. TDK’s defense depends entirely on the high-value 8.48% CAGR Automotive segment.</div>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.6, 1])
    with col1:
        st.write("#### Market Decoupling: Revenue vs. Physical Unit Production")
        df = data["rev_vol"]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Year"], y=df["Revenue ($Mn)"], name="Revenue ($Mn)", line=dict(color=BURGUNDY, width=4)))
        fig.add_trace(go.Bar(x=df["Year"], y=df["Units (Bn)"], name="Units (Bn)", yaxis="y2", marker_color=GOLD, opacity=0.5))
        fig.update_layout(yaxis=dict(title="Revenue ($Mn)"), yaxis2=dict(title="Units (Bn)", overlaying="y", side="right", showgrid=False))
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.write("#### Chapter 2: Segment Trajectory Teaser")
        st.write("Detailed 10-year volume indices by 15 device sub-categories.")
        st.markdown("""<div class="blurred">| Category | 2025 Bn | 2035 Bn | CAGR |<br>| --- | --- | --- | --- |<br>| Flagship 5G | 22.4 | 31.8 | 3.6% |<br>| EV Chassis | 3.5 | 10.5 | 11.6% |</div>""", unsafe_allow_html=True)
        render_teaser_lock()

def render_value_dynamics(data):
    st.markdown('<div class="hero"><h2>Pillar 2: Pricing & Device Engines</h2><p>Chapters 3-6: ASP Hierarchies and the transition from Smartphones to EVs.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Chapter 3: The Reliability Premium Index ($/unit)")
        df_p = data["pricing"]
        fig = px.bar(df_p, x="Segment", y=["2025 ASP ($)", "2035 ASP ($)"], barmode="group", color_discrete_sequence=[BURGUNDY_DARK, GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
        st.info("💡 Only Automotive-Qualified inductors show positive price appreciation (+0.54% CAGR) through 2035.")

    with col2:
        st.write("#### Chapters 4-6: Device Content Multipliers (Units/Device)")
        df_d = data["devices"]
        fig = px.bar(df_d, x="Category", y=["2025 Bn units", "2035 Bn units"], barmode="group", color_discrete_sequence=[BURGUNDY_MID, GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)

    section_title = "Smartphone Content Evolution ($ per handset)"
    st.write(f"#### {section_title}")
    st.write("Detailed RF Front-end cost-per-handset modeling for the top 5 global OEMs.")
    st.markdown("""<div class="blurred">| OEM | 5G RF Inductor Content | 6G Pre-load | Pricing Moat |<br>| --- | --- | --- | --- |<br>| OEM A | [HIDDEN] | [HIDDEN] | High |<br>| OEM B | [HIDDEN] | [HIDDEN] | Medium |</div>""", unsafe_allow_html=True)
    render_teaser_lock("Full Smartphone content indices available in Chapter 4.")

def render_miniaturization_apps(data):
    st.markdown('<div class="hero"><h2>Pillar 3: Use-Cases & Tech Moats</h2><p>Chapters 7-8: 01005 Miniaturization and Automotive Power-over-Coax (PoC).</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.3])
    with col1:
        st.write("#### Chapter 8: Architecture Migration (Unit %)")
        fig = px.bar(data["mini"], x="Year", y=["Standard (0402+)", "Precision (0201)", "Elite (01005)"], barmode="stack", color_discrete_sequence=[BURGUNDY_DARK, BURGUNDY_MID, GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.write("#### Chapter 7: Revenue Shift by Use-Case")
        df_a = data["apps"]
        fig = px.bar(df_a, x="App", y=["Share 2025 (%)", "Share 2035 (%)"], barmode="group", color_discrete_sequence=[BURGUNDY, GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    st.markdown("""<div class="insight-box"><strong>Tech Barrier:</strong> Sub-0402 architectures for Automotive PoC networks represent TDK's primary margin defense. Challenger yields in 01005 remain <60%, providing a 3-5 year window of elite pricing dominance.</div>""", unsafe_allow_html=True)

def render_supply_geopolitics(data):
    st.markdown('<div class="hero"><h2>Pillar 4: Supply Chain & Geopolitics</h2><p>Chapters 9-11 & 16-17: Regional hotspots, "China+1", and Tariff Impact.</p></div>', unsafe_allow_html=True)
    
    section_title = "Global Opportunity Map 2035 ($Mn)"
    st.write(f"#### {section_title}")
    fig = px.choropleth(data["regions"], locations="MapCode", color="2035 Rev ($Mn)", color_continuous_scale=[[0, "#FAF5F7"], [0.5, GOLD], [1, BURGUNDY]], hover_name="Region")
    fig.update_layout(geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular', bgcolor='rgba(0,0,0,0)'))
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Chapter 16: Manufacturing Footprint Shift")
        st.write("Shift in Volume Share (%) toward ASEAN / Vietnam hubs.")
        df_f = pd.DataFrame({"Region": ["Japan Anchor", "China Primary", "ASEAN+", "RoW"], "Shift": [-0.5, 1.0, 0.8, -1.3]})
        fig = px.bar(df_f, x="Region", y="Shift", color="Shift", color_continuous_scale=[[0, BURGUNDY], [1, GOLD]])
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.write("#### Chapter 17: Landed Cost Multipliers (Tariff-Adjusted)")
        df_t = data["tariffs"]
        fig = px.line(df_t, x="Geography", y="Combined Multiplier", markers=True, color_discrete_sequence=[GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
        st.warning("⚠️ US IEEPA 20% Tariffs elevate landed component costs to a 1.188 multiplier in the US corridor.")

def render_competition_tdk(data):
    st.markdown('<div class="hero"><h2>Pillar 5: Competition & TDK Strategy</h2><p>Chapters 12-15 & 19-20: Oligopoly Control and Final Playbook.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.4])
    with col1:
        st.write("#### Chapter 12: Core Market Share (2035)")
        fig = px.pie(data["comp"], values="2025 Share (%)", names="Company", hole=0.6, color_discrete_sequence=[BURGUNDY, GOLD, BURGUNDY_MID, "#A45A7B", "#CBD5E1", "#E5E7EB"])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.write("#### Chapter 13: Tier 1 Strategic Alignment Score")
        df_strat = pd.DataFrame({
            "Capability": ["Material Science", "Auto AEC-Q200", "01005 Yield", "PoC Integration", "Local China Cost"],
            "Murata": [5, 5, 5, 4, 3],
            "TDK (Client)": [5, 5, 5, 5, 2],
            "Samsung EM": [4, 5, 3, 3, 4]
        })
        st.table(df_strat)
    
    st.write("#### Chapter 19: TDK Win/Loss Matrix")
    st.markdown("""
    | Segment | TDK Position | Strategic Verdict | Priority |
    | --- | --- | --- | --- |
    | **Auto PoC Networks** | Elite Advantage | WIN: Monopolize Reference Designs | Tier 1 |
    | **Sub-0402 RF** | Competitive | WIN: Aggressive R&D Acceleration | Tier 1 |
    | **Standard NFC** | Cost Disadvantage | DEFEND: Automate or License Out | Tier 2 |
    """)

    st.subheader("Chapter 20: Investment & ROI Projections (LOCKED)")
    st.write("NPV and Payback Year modeling for the Ouchi Factory retooling initiative.")
    st.markdown("""<div class="blurred">| Investment Area | CapEx ($M) | Payback (Yr) | Terminal Value |<br>| --- | --- | --- | --- |<br>| 6G Ceramic Lab | [REDACTED] | 2029 | High |<br>| ASEAN Scale-up | [REDACTED] | 2027 | High |</div>""", unsafe_allow_html=True)
    render_teaser_lock()

# =========================
# ACCESS GATEWAY
# =========================
def check_access():
    expected_password = str(st.secrets.get("ACCESS_CODE", "SMR2026")).strip()
    if "authenticated" not in st.session_state: st.session_state.authenticated = False
    if st.session_state.authenticated: return True

    if LOGO_B64:
        st.markdown(f'<div style="text-align:center; margin-top:10vh;"><img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:65px;" /></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        with st.form("login_form"):
            st.markdown(f"<h3 style='text-align:center; color:{BURGUNDY}; font-weight:800;'>🔐 Boardroom Authentication</h3>", unsafe_allow_html=True)
            name = st.text_input("Executive Name*")
            password = st.text_input("Access Code*", type="password")
            enter = st.form_submit_button("Enter Boardroom", use_container_width=True)

    if enter:
        if password.strip() == expected_password:
            st.session_state.authenticated = True
            st.session_state.viewer_name = name.strip()
            st.rerun()
        else: st.error("❌ Invalid Access Code.")
    st.stop()

# =========================
# MAIN DASHBOARD ENTRY
# =========================
check_access()
data = load_data()

with st.sidebar:
    brand_sidebar()
    st.markdown(f'<div class="viewer-chip">Verified: {st.session_state.viewer_name}</div>', unsafe_allow_html=True)
    
    page = st.sidebar.radio("", [
        "1. Executive & Market Core",
        "2. Pricing & Demand Engines",
        "3. Miniaturization & Apps",
        "4. Geopolitics & Supply",
        "5. Competitive & TDK Strategy",
        "6. Methodology & Appendix"
    ])
    
    st.markdown("---")
    if st.button("🔒 End Secure Session", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ROUTING
if "1." in page: render_market_core(data)
elif "2." in page: render_value_dynamics(data)
elif "3." in page: render_miniaturization_apps(data)
elif "4." in page: render_supply_geopolitics(data)
elif "5." in page: render_competition_tdk(data)
else:
    st.markdown(f'<div class="hero"><h2>Methodology & Detailed Appendix</h2><p>Bottom-up device shipment modeling vs. regional supplier capacity benchmarks.</p></div>', unsafe_allow_html=True)
    st.info("Full bibliography (450+ sources) and city-level demand indices are available in the full deliverable.")
    st.markdown("### Coverage Matrix")
    st.write("Includes 15 device categories, 25 major OEMs, and 45 country corridors.")
