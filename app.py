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
    page_title="Strategic Market Research | TDK Corporation Advisory",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded", 
)

# =========================
# THEME COLORS
# =========================
BURGUNDY = "#4A0C25" 
BURGUNDY_DARK = "#2D0716"
BURGUNDY_MID = "#7A143D"
GOLD = "#C49A23"
INK = "#1A1A1A"
MUTED = "#6B7280"
BORDER = "#E5E7EB"

PREVIEW_NOTE = "SMR Confidential. Unit-level projections and competitive cost curves are restricted."

@st.cache_data
def load_logo_base64() -> str | None:
    # Looks for your uploaded logo
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

    /* --- INPUT FIELDS & BUTTONS --- */
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
        padding: 8px 12px !important; margin-bottom: 2px !important; border-radius: 8px !important;
    }}
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[checked]) {{
         background: rgba(255,255,255,0.1) !important; border-left: 4px solid {GOLD} !important;
    }}
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] p {{ color: white !important; font-size: 0.88rem !important; }}

    /* HERO & CARDS */
    .hero {{
      background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_MID} 100%);
      color: white; border-radius: 16px; padding: 34px 40px; margin-bottom: 32px; position: relative; overflow: hidden;
    }}
    .metric-card {{
      background: white; border: 1px solid #E5E7EB; border-radius: 12px; padding: 24px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: all 0.3s ease;
    }}
    .metric-label {{ color: {MUTED}; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; }}
    .metric-value {{ color: {BURGUNDY}; font-size: 2.2rem; font-weight: 800; line-height: 1; }}
    
    .insight-box {{
      background: #ffffff; border-left: 6px solid {GOLD}; border-radius: 8px; padding: 20px 24px;
      margin-bottom: 24px; box-shadow: 0 8px 24px rgba(196,154,35,0.05);
    }}
    
    /* TEASER / LOCKED UI */
    .locked-overlay {{
        background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 90%);
        padding: 40px; text-align: center; border-radius: 0 0 12px 12px; margin-top: -60px; position: relative; z-index: 10;
    }}
    .blurred {{ filter: blur(4px); opacity: 0.4; pointer-events: none; }}
    
    .viewer-chip {{
      display:inline-block; padding:6px 12px; border-radius:999px; font-size:0.75rem; font-weight:700;
      background: rgba(255,255,255,0.1); color: {GOLD}; margin-top:10px; margin-bottom: 10px;
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
    logo_html = f'<img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:48px; width:auto; margin-bottom:12px; filter: brightness(0) invert(1);" />' if LOGO_B64 else ""
    st.sidebar.markdown(f'<div class="smr-brand">{logo_html}<h1 style="color:white; margin:0; font-size:1.1rem; font-weight:800; letter-spacing:-0.02em; line-height:1.2;">Strategic Market Research</h1><p style="color:rgba(255,255,255,0.6); margin:4px 0 0 0; font-size:0.82rem; font-weight:500;">Multilayer Inductor Market<br>Executive Boardroom</p></div>', unsafe_allow_html=True)

def card_metric(label: str, value: str, foot: str):
    st.markdown(f'<div class="metric-card"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div style="color:{MUTED}; font-size:0.8rem; margin-top:8px;">{foot}</div></div>', unsafe_allow_html=True)

def chart_theme(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=INK, family="Plus Jakarta Sans"),
        margin=dict(l=10, r=10, t=40, b=10), legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="rgba(0,0,0,0.05)", zeroline=False)
    return fig

def render_teaser_lock(text="Full dataset unlocked with report purchase."):
    st.markdown(f"""
    <div class="locked-overlay">
        <p style="color:{BURGUNDY}; font-weight:800; font-size:1.1rem;">🔒 ACCESS RESTRICTED</p>
        <p style="color:{MUTED}; font-size:0.9rem; margin-bottom:15px;">{text}</p>
        <button style="background:{BURGUNDY}; color:white; border:none; padding:8px 20px; border-radius:6px; font-weight:700; cursor:pointer;">Request Unlock</button>
    </div>
    """, unsafe_allow_html=True)

# =========================
# DATA ENGINE
# =========================
@st.cache_data
def load_data():
    data = {}
    data["market_rev"] = pd.DataFrame({
        "Year": ["2025", "2027", "2029", "2031", "2033", "2035"],
        "RF / High-Freq ($Mn)": [839.1, 890.0, 950.0, 1010.0, 1080.0, 1143.4],
        "Auto-Qualified ($Mn)": [132.8, 155.0, 185.0, 220.0, 260.0, 299.6],
        "Compact Ferrite ($Mn)": [474.8, 510.0, 545.0, 585.0, 630.0, 672.2]
    })
    data["units"] = pd.DataFrame({"Year": ["2025", "2035"], "Total Units (Bn)": [77.0, 116.1]})
    return data

# =========================
# RENDER VIEWS
# =========================
def render_executive(data):
    st.markdown('<div class="hero"><h2>Executive Strategy Summary</h2><p>Global Multilayer Inductor Market (2025–2035). Strategic analysis and positioning for TDK Corporation.</p></div>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: card_metric("2035 Revenue Ceiling", "$2.12 Bn", "Projected total market value.")
    with c2: card_metric("Auto-Grade CAGR", "8.48%", "Primary high-margin engine.")
    with c3: card_metric("Unit Volume 2035", "116.1 Bn", "Global manufacturing load.")
    with c4: card_metric("01005 Index", "Elite", "Maximum tech qualification.")

    st.markdown("""
    <div class="insight-box">
        <strong>Strategic Directive (Chapters 1-3):</strong> Value creation is rapidly decoupling from pure unit volumes. 
        TDK must prioritize 165°C thermal stability and ultra-high-frequency (UHF) RF matching as the primary defense 
        against the 3.5% CAGR commodity price erosion in consumer segments.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("Market Expansion Trajectory by Key Segment ($Mn)")
        df = data["market_rev"]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Year"], y=df["RF / High-Freq ($Mn)"], name="RF / High-Freq", line=dict(color=BURGUNDY, width=4), stackgroup='one'))
        fig.add_trace(go.Scatter(x=df["Year"], y=df["Compact Ferrite ($Mn)"], name="Compact Ferrite", line=dict(color=BURGUNDY_MID, width=1), stackgroup='one'))
        fig.add_trace(go.Scatter(x=df["Year"], y=df["Auto-Qualified ($Mn)"], name="Automotive-Qualified", line=dict(color=GOLD, width=3), stackgroup='one'))
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.subheader("Price Hierarchy Shift (2025 vs 2035)")
        st.write("Unit prices for Automotive-grade are projected to appreciate, unlike consumer segments.")
        df_p = pd.DataFrame({
            "Segment": ["Auto Grade", "RF High-Q", "Standard Ferrite"],
            "2025 ASP ($)": [0.0360, 0.0220, 0.0135],
            "2035 ASP ($)": [0.0380, 0.0210, 0.0125]
        })
        fig = px.bar(df_p, x="Segment", y=["2025 ASP ($)", "2035 ASP ($)"], barmode="group", color_discrete_sequence=[BURGUNDY_DARK, GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)

def render_engines():
    st.markdown('<div class="hero"><h2>Device-Level Demand Engines</h2><p>Chapters 4-6: From 5G Smartphones to EV Traction Inverters & IoT Modules.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Inductor Content Multiple (Units/Device)")
        df_c = pd.DataFrame({"Device": ["Smartphone", "EV", "IoT Module", "Earwear"], "Content": [45, 140, 4, 18]})
        fig = px.bar(df_c.sort_values("Content"), x="Content", y="Device", orientation="h", color="Content", color_continuous_scale=[[0, GOLD], [1, BURGUNDY]])
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.subheader("Global Project Pipeline (Sample)")
        st.write("Preview of 2,000+ row database of named EV and 5G infrastructure rollouts.")
        st.markdown("""
        <div class="blurred">
        | Project Name | Region | Expected Units | Launch Year |
        | --- | --- | --- | --- |
        | Project Alpha-9 | APAC | 5.2 Bn | 2027 |
        | Tesla Giga V | NA | 1.8 Bn | 2028 |
        | Vodafone 6G Test | EU | 0.9 Bn | 2031 |
        </div>
        """, unsafe_allow_html=True)
        render_teaser_lock("Full Project Database contains specific 5G city-level rollout indices.")

def render_miniaturization():
    st.markdown('<div class="hero"><h2>Miniaturization & Tech Moats</h2><p>Chapter 8: The transition to 01005 architectures and embedded passives.</p></div>', unsafe_allow_html=True)
    
    st.subheader("Component Size Migration (Unit Share %)")
    df_sz = pd.DataFrame({
        "Year": ["2025", "2030", "2035"],
        "0603/0402": [40, 25, 10],
        "0201": [50, 55, 45],
        "01005 (Elite)": [10, 20, 45]
    })
    fig = px.bar(df_sz, x="Year", y=["0603/0402", "0201", "01005 (Elite)"], barmode="stack", color_discrete_sequence=[BURGUNDY_DARK, BURGUNDY_MID, GOLD])
    st.plotly_chart(chart_theme(fig), use_container_width=True)
    st.markdown('<div class="insight-box"><strong>Tech Moat:</strong> 01005 architectures represent an impenetrable technical barrier for 80% of regional challengers. Mastering photolithography at this scale is TDK\'s primary margin defender.</div>', unsafe_allow_html=True)

def render_regional():
    st.markdown('<div class="hero"><h2>Geographic Concentration & Tariffs</h2><p>Chapters 9-11 & 17: Analyzing the "China+1" supply chain realignment.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2035 Regional Revenue Hotspots")
        df_reg = pd.DataFrame({"Region": ["China", "India", "USA", "Germany", "Japan"], "Rev": [560, 253, 215, 66, 73]})
        fig = px.pie(df_reg, values="Rev", names="Region", hole=0.5, color_discrete_sequence=[BURGUNDY, GOLD, BURGUNDY_MID, BURGUNDY_SOFT, BORDER])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.subheader("Combined Market Multipliers (Landed Cost)")
        st.write("Factoring in the impact of US Section 122 and IEEPA 20% tariffs.")
        df_t = pd.DataFrame({
            "Geography": ["United States", "Germany", "Japan", "Vietnam (Bypass)"],
            "Multiplier": [1.188, 1.145, 1.134, 0.836]
        })
        fig = px.line(df_t, x="Geography", y="Multiplier", markers=True, color_discrete_sequence=[GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
        render_teaser_lock("Tariff sensitivity analysis for 15 specific country corridors available in Chapter 17.")

def render_competitive():
    st.markdown('<div class="hero"><h2>Competitive Control & Value Chain</h2><p>Chapters 12-16: The Japanese Oligopoly vs. Regional Challengers.</p></div>', unsafe_allow_html=True)
    
    st.subheader("Tier 1 Strategic Capability Matrix (1-5)")
    st.write("How TDK and Murata defend against Samsung EM and YAGEO.")
    df_cap = pd.DataFrame({
        "Company": ["TDK (Client)", "Murata", "Samsung EM", "Taiyo Yuden", "Sunlord"],
        "Material Science": [5, 5, 4, 5, 3],
        "Auto AEC-Q200": [5, 5, 5, 4, 3],
        "01005 Yields": [5, 5, 4, 3, 2],
        "Margin Health": ["Elite", "Elite", "High", "Mid", "Pressure"]
    })
    st.table(df_cap)
    
    st.subheader("Value Chain Profit Pools (2035 Model)")
    df_vc = pd.DataFrame({
        "Segment": ["Material Formulation", "Patterning/Layering", "Sintering", "Testing & Qualification"],
        "Share of Profit": [35, 15, 10, 40]
    })
    fig = px.bar(df_vc, x="Share of Profit", y="Segment", orientation="h", color_discrete_sequence=[GOLD])
    st.plotly_chart(chart_theme(fig), use_container_width=True)
    st.info("Testing & Qualification generates the highest EBITDA per unit due to safety-critical certification premiums.")

def render_tdk_strategy():
    st.markdown('<div class="hero"><h2>TDK Win/Loss Matrix & Playbook</h2><p>Chapters 19-20: Final strategic recommendations and investment roadmap.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Strategic Playbook: Priorities")
        st.markdown("""
        - **WIN:** Automotive Power-over-Coax (PoC)
        - **WIN:** Sub-0402 RF Matching
        - **DEFEND:** Compact Ferrite (NFC)
        - **AVOID:** Low-Q standardized generic kits
        """)
    with col2:
        st.subheader("Investment Roadmap ($Mn)")
        st.write("Recommended allocation of R&D capital through 2035.")
        st.markdown("""
        <div class="blurred">
        | Initiative | Value Pool | Priority | CapEx |
        | --- | --- | --- | --- |
        | Ouchi Factory Retooling | $42.3M | Tier 1 | [HIDDEN] |
        | 6G Ceramic dielectric | $63.5M | Tier 1 | [HIDDEN] |
        </div>
        """, unsafe_allow_html=True)
        render_teaser_lock("Detailed NPV and ROI analysis for CapEx initiatives is restricted.")

# =========================
# AUTH GATEWAY
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
            st.markdown(f"<h3 style='text-align:center; color:{BURGUNDY}; font-weight:800;'>🔐 Executive Authentication</h3>", unsafe_allow_html=True)
            name = st.text_input("Full Name*")
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
# MAIN ENTRY
# =========================
check_access()
data = load_data()

with st.sidebar:
    brand_sidebar()
    st.markdown(f'<div class="viewer-chip">Verified: {st.session_state.viewer_name}</div>', unsafe_allow_html=True)
    
    page = st.sidebar.radio("", [
        "1. Executive Strategy",
        "2. Demand Engines (Mobile/Auto)",
        "3. Miniaturization Moats",
        "4. Regional & Tariff Analysis",
        "5. Competitive Control",
        "6. TDK Strategic Playbook",
        "7. Methodology & Appendix"
    ])
    
    st.markdown("---")
    if st.button("🔒 End Secure Session", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ROUTING
if "1." in page: render_executive(data)
elif "2." in page: render_engines()
elif "3." in page: render_miniaturization()
elif "4." in page: render_regional()
elif "5." in page: render_competitive()
elif "6." in page: render_tdk_strategy()
else:
    st.markdown(f'<div class="hero"><h2>Methodology & Appendix</h2><p>Triangulated bottom-up modeling vs. supplier capacity benchmarks.</p></div>', unsafe_allow_html=True)
    st.info("Full bibliography and 450-row country/city level demand indices available in the purchased deliverable.")
