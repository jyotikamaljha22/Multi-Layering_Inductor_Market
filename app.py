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
    page_title="Strategic Market Research | TDK Corporation",
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

PREVIEW_NOTE = (
    "SMR Confidential: Access restricted. Detailed unit-level data and competitive pricing "
    "yields are available in the full premium report."
)

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

    /* INPUT FIELDS */
    .stTextInput input {{
        border-radius: 8px !important; border: 1px solid #E5E7EB !important;
        padding: 12px 14px !important; background-color: #ffffff !important; color: #1A1A1A !important;
    }}

    /* BUTTONS */
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
      color: white; border-radius: 16px; padding: 34px 40px; margin-bottom: 32px;
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
    
    .locked-table {{
        filter: blur(2px); opacity: 0.5; pointer-events: none;
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
# HELPERS
# =========================
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

# =========================
# DATA ENGINE
# =========================
@st.cache_data
def load_data():
    data = {}
    # Overview
    data["overview"] = pd.DataFrame({
        "Year": ["2025", "2027", "2029", "2031", "2033", "2035"],
        "Revenue ($Mn)": [1446.7, 1550.0, 1665.0, 1800.0, 1950.0, 2115.3],
        "Units (Bn)": [77.0, 83.2, 90.1, 98.4, 107.0, 116.1]
    })
    # Pricing
    data["pricing"] = pd.DataFrame({
        "Segment": ["RF / High-Freq", "Compact Ferrite", "Automotive-Qualified"],
        "2025 Price ($)": [0.0220, 0.0135, 0.0360],
        "2035 Price ($)": [0.0210, 0.0125, 0.0380],
        "Trend": ["Deflationary", "Deflationary", "Appreciating"]
    })
    # TDK Position
    data["tdk_strategy"] = pd.DataFrame({
        "Target Segment": ["Auto-Qualified", "RF High-Freq", "Compact Ferrite"],
        "TDK Advantage": ["Elite / AEC-Q200", "High-Q Leadership", "Scale-Locked"],
        "Priority": ["Tier 1", "Tier 1", "Tier 2"]
    })
    return data

# =========================
# VIEWS
# =========================
def render_overview(data):
    st.markdown(f'<div class="hero"><h2>Executive Strategy Summary</h2><p>Global Multilayer Inductor Market (2025–2035). Strategic analysis for TDK Corporation leadership.</p></div>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: card_metric("2035 TAM", "$2.12 Bn", "Projected total market value.")
    with c2: card_metric("Unit CAGR", "4.19%", "Physical manufacturing expansion.")
    with c3: card_metric("Price Delta", "-0.32%", "Blended market price erosion.")
    with c4: card_metric("Auto Share", "14.1%", "High-value segment penetration.")

    st.markdown('<div class="insight-box"><strong>Strategic Imperative:</strong> Market expansion is decoupling from pure unit volume. TDK must prioritize thermal reliability thresholds and 01005 miniaturization to defend margins against regional commodity challengers.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("Global Market Trajectory: Revenue vs physical Volume")
        df = data["overview"]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Year"], y=df["Revenue ($Mn)"], name="Revenue ($Mn)", line=dict(color=BURGUNDY, width=4)))
        fig.add_trace(go.Bar(x=df["Year"], y=df["Units (Bn)"], name="Units (Bn)", yaxis="y2", marker_color=GOLD, opacity=0.6))
        fig.update_layout(yaxis=dict(title="Revenue ($Mn)"), yaxis2=dict(title="Volume (Bn units)", overlaying="y", side="right", showgrid=False))
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.subheader("Structural Revenue Shift (2035)")
        # Teasing the shift toward Automotive
        fig = px.pie(values=[54, 32, 14], names=["RF / High-Freq", "Compact Ferrite", "Automotive"], hole=0.6, 
                     color_discrete_sequence=[BURGUNDY_DARK, BURGUNDY_MID, GOLD])
        st.plotly_chart(chart_theme(fig), use_container_width=True)

def render_pricing(data):
    st.markdown('<div class="hero"><h2>Pricing & Value Dynamics</h2><p>Chapter 3: Analysis of ASP hierarchies and deflationary moats.</p></div>', unsafe_allow_html=True)
    
    st.write("### The Pricing Hierarchy ($ per unit)")
    fig = px.bar(data["pricing"], x="Segment", y=["2025 Price ($)", "2035 Price ($)"], barmode="group",
                 color_discrete_sequence=[BURGUNDY, GOLD])
    st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    st.markdown('<div class="insight-box"><strong>Pricing Note:</strong> Automotive-qualified inductors represent the only category demonstrating positive price appreciation over the decade. All other segments require volume to offset ASP erosion.</div>', unsafe_allow_html=True)

def render_demand_engines():
    st.markdown('<div class="hero"><h2>Demand Engines & Device Modeling</h2><p>Chapters 4-6: From Smartphones to EVs and IoT modules.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Device Content Multiplier (Units/Device)")
        df_dev = pd.DataFrame({
            "Device": ["Smartphone (5G)", "Smartwatch", "EV Chassis", "IoT Module"],
            "Inductor Content": [45, 18, 140, 4]
        })
        fig = px.bar(df_dev, x="Device", y="Inductor Content", color_discrete_sequence=[BURGUNDY_MID])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
        
    with col2:
        st.subheader("Strategic Growth Pools (2035)")
        st.write("A detailed 2,000-row project database for named IoT and EV rollouts is available in the full report.")
        st.info("🔒 Named Project Database: LOCKED (Access required)")
        st.markdown('<div class="locked-table">| Project | Capacity | Region | Units |<br>| --- | --- | --- | --- |<br>| [REDACTED] | 1.2M | APAC | 5.4Bn |</div>', unsafe_allow_html=True)

def render_competitive():
    st.markdown('<div class="hero"><h2>Competitive Landscape</h2><p>Chapters 12-14: Market share control and challenger positioning.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Core Market Control (2025 Share)")
        shares = pd.DataFrame({
            "Competitor": ["Murata", "TDK", "Samsung EM", "Taiyo Yuden", "Regional Challengers"],
            "Share": [31, 22, 9, 8, 30]
        })
        fig = px.pie(shares, values="Share", names="Competitor", hole=0.5, color_discrete_sequence=[BURGUNDY, GOLD, BURGUNDY_MID, BURGUNDY_SOFT, "#E5E7EB"])
        st.plotly_chart(chart_theme(fig), use_container_width=True)
    
    with col2:
        st.subheader("Capability Benchmarking (1-5)")
        st.write("How challengers (Sunlord, YAGEO) are moving up the tech curve.")
        df_cap = pd.DataFrame({
            "Competitor": ["TDK", "Murata", "Sunlord", "YAGEO"],
            "RF Precision": [5, 5, 3, 2],
            "Auto Grade": [5, 5, 3, 2],
            "01005 Scaling": [5, 5, 2, 1]
        })
        st.dataframe(df_cap, use_container_width=True, hide_index=True)

def render_tdk_strategy(data):
    st.markdown('<div class="hero"><h2>TDK Strategic Roadmap</h2><p>Chapter 19-20: Segment prioritization and win/loss matrix.</p></div>', unsafe_allow_html=True)
    
    st.subheader("Segment Opportunity Mapping")
    st.table(data["tdk_strategy"])
    
    st.markdown("""
    <div class="insight-box">
        <strong>Final Recommendation:</strong> TDK must utilize its elite Japanese manufacturing nodes (e.g., Ouchi Factory) purely as specialized capability anchors. 
        <strong>Immediate Capital Allocation:</strong> Relentless expansion of AEC-Q200 production capacity for Power-over-Coax (PoC) automotive networks.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Investment Priority Index (LOCKED)")
    st.write("Detailed NPV and ROI analysis for the Ouchi expansion is reserved for report holders.")
    st.button("Request Unlock: Financial Valuation Appendix")

# =========================
# AUTH GATEWAY
# =========================
def check_access():
    expected_password = str(st.secrets.get("ACCESS_CODE", "SMR2026")).strip()
    if "authenticated" not in st.session_state: st.session_state.authenticated = False
    if st.session_state.authenticated: return True

    if LOGO_B64:
        st.markdown(f'<div style="text-align:center; margin-top:8vh;"><img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:60px;" /></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 5vh;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        with st.form("login_form"):
            st.markdown(f"<h3 style='text-align:center; color:{BURGUNDY};'>🔐 Executive Access</h3>", unsafe_allow_html=True)
            name = st.text_input("Name*")
            email = st.text_input("Email*")
            password = st.text_input("Access Code*", type="password")
            enter = st.form_submit_button("Enter Dashboard", use_container_width=True)

    if enter:
        if password.strip() == expected_password:
            st.session_state.authenticated = True
            st.session_state.viewer_name = name.strip()
            st.rerun()
        else: st.sidebar.error("❌ Invalid Access Code.")
    st.stop()

# =========================
# MAIN APP
# =========================
check_access()
data = load_data()

with st.sidebar:
    brand_sidebar()
    st.markdown(f'<div class="viewer-chip">Verified: {st.session_state.viewer_name}</div>', unsafe_allow_html=True)
    
    page = st.sidebar.radio("", [
        "Executive Strategy",
        "Pricing & Value Dynamics",
        "Demand Engines (Mobile/Auto)",
        "Competitive Landscape",
        "TDK Strategic Playbook",
        "Appendix & Methodology"
    ])
    
    st.markdown("---")
    if st.button("End Session", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

if page == "Executive Strategy": render_overview(data)
elif page == "Pricing & Value Dynamics": render_pricing(data)
elif page == "Demand Engines (Mobile/Auto)": render_demand_engines()
elif page == "Competitive Landscape": render_competitive()
elif page == "TDK Strategic Playbook": render_tdk_strategy(data)
else:
    st.markdown(f'<div class="hero"><h2>Methodology & Appendix</h2><p>Data triangulated via bottom-up device shipment modeling and regional supplier capacity checks.</p></div>', unsafe_allow_html=True)
    st.info("Full bibliography and 450-row country/city level demand indices available in the purchased deliverable.")