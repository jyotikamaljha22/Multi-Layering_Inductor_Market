import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Global Multilayer Inductor Market (2025–2035)",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# BRAND SYSTEM
# -----------------------------
BURGUNDY = "#5B0F2E"
BURGUNDY_DARK = "#431024"
BURGUNDY_LIGHT = "#7A163F"
BURGUNDY_SOFT = "#F7EEF2"
ROSE = "#E8C7D5"
INK = "#0F172A"
SLATE = "#475569"
SLATE_LIGHT = "#64748B"
BORDER = "#E5E7EB"
BG = "#F6F2F4"
WHITE = "#FFFFFF"

PRIMARY_PASSWORD = "SMR2026"
CLIENT_NAME = "TDK Corporation"
CHART_ANCHOR = "<!--CHART_ANCHOR-->"

QUICK_METRICS = {
    "Market Revenue 2035": "$2,115.25Mn",
    "Global CAGR": "3.87%",
    "TDK 2025 Proxied": "$318.27Mn",
    "Premium Growth Vector": "Automotive",
}

# -----------------------------
# DATA / CONTENT
# -----------------------------
# IMPORTANT:
# Paste your full CHAPTERS dictionary here exactly as-is from your existing file.
# Do not change the HTML content unless you want copy edits.
CHAPTERS = {
    # >>> PASTE YOUR CURRENT FULL 1–20 CHAPTERS DICTIONARY HERE <<<
}

# -----------------------------
# CONFIDENTIALITY OVERRIDES
# -----------------------------
COMPETITOR_ALIAS_MAP = {
    "Murata": "Player 1",
    "TDK Corporation": "Player 2",
    "Samsung Electro-Mechanics": "Player 3",
    "Samsung E-M": "Player 3",
    "Taiyo Yuden": "Player 4",
    "Sunlord": "Player 5",
    "YAGEO / Chilisin": "Player 6",
}

CH11_TITLE = "11. Competitive Landscape & Market Share"

def anonymize_chapter_11(html: str) -> str:
    for original, alias in COMPETITOR_ALIAS_MAP.items():
        html = html.replace(original, alias)
    html = html.replace(
        "Japanese manufacturers, with Player 1 and Player 2 collectively commanding over half of the global revenue pool.",
        "leading manufacturers, with Player 1 and Player 2 collectively commanding over half of the global revenue pool."
    )
    html = html.replace("legacy Japanese manufacturers", "legacy incumbents")
    return html

if CH11_TITLE in CHAPTERS:
    CHAPTERS[CH11_TITLE] = anonymize_chapter_11(CHAPTERS[CH11_TITLE])

# -----------------------------
# DATA FOR VISUALS
# -----------------------------
market_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Revenue": [1446.68, 1727.53, 2115.25],
    "Volume": [85.39, 112.51, 146.40],
    "ASP": [0.0169, 0.0153, 0.0144],
})

tam_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Device Anchors": [5108.50, 6518.08, 8389.83],
    "Components per Device": [16.7, 17.2, 17.4],
})

segment_df = pd.DataFrame({
    "Segment": ["Radio Frequency (RF)", "Compact Ferrite / NFC", "Automotive-Qualified"],
    "2025": [839.12, 474.80, 132.75],
    "2030": [973.82, 560.10, 193.61],
    "2035": [1143.43, 672.21, 299.60],
})

device_df = pd.DataFrame({
    "Device": ["Smartphones", "Earwear / TWS", "Smartwatches", "Electric Vehicles (EVs)", "ICE / HEV Vehicles", "IoT Edge Modules"],
    "2025": [1240.00, 360.00, 206.00, 25.00, 67.50, 3200.00],
    "2030": [1316.20, 437.99, 262.88, 39.00, 62.00, 4400.00],
    "2035": [1397.09, 532.88, 335.55, 61.95, 56.28, 6006.83],
})

pricing_df = pd.DataFrame({
    "Segment": ["Radio Frequency (RF)", "Compact Ferrite / NFC", "Automotive-Qualified", "Blended Device Metric (Smartphone)"],
    "2025": [0.0220, 0.0135, 0.0350, 0.0186],
    "2030": [0.0215, 0.0130, 0.0340, 0.0181],
    "2035": [0.0210, 0.0125, 0.0330, 0.0176],
})

north_america_df = pd.DataFrame({
    "Region": ["United States", "Mexico (Production Hub)", "Canada / Rest of NA"],
    "2025": [146.58, 17.68, 22.40],
    "2030": [177.30, 21.41, 26.10],
    "2035": [214.83, 25.91, 31.10],
})

europe_df = pd.DataFrame({
    "Region": ["Germany", "United Kingdom", "France & Italy", "Eastern Europe (Assembly)"],
    "2025": [41.97, 18.10, 26.40, 14.20],
    "2030": [52.54, 21.40, 31.20, 17.80],
    "2035": [65.75, 25.80, 37.90, 22.50],
})

apac_df = pd.DataFrame({
    "Region": ["China", "India", "Japan", "South Korea", "Taiwan", "Vietnam"],
    "2025": [398.24, 124.96, 51.70, 32.54, 8.45, 17.15],
    "2030": [470.83, 180.37, 61.35, 38.16, 10.03, 21.90],
    "2035": [559.87, 253.32, 72.97, 44.80, 11.89, 27.98],
})

competitive_df = pd.DataFrame({
    "Competitor": ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Others"],
    "2025": [31.0, 22.0, 9.0, 8.0, 7.0, 6.0, 3.0, 14.0],
    "2035": [28.0, 21.0, 10.0, 8.0, 10.0, 8.0, 3.0, 12.0],
})

scenario_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Base Case Reality": [1446.68, 1727.53, 2115.25],
    "Optimized Upside": [1578.90, 1885.43, 2308.58],
    "Constrained Downside": [1305.05, 1558.41, 1908.16],
})

roadmap_df = pd.DataFrame({
    "Priority": ["Automotive Dominance", "Geopolitical Resilience", "Miniaturization Parity", "Portfolio Optimization"],
    "Priority Score": [95, 86, 89, 78],
    "Time Horizon": ["Near-term", "Near-term", "Mid-term", "Immediate"],
})

miniaturization_df = pd.DataFrame({
    "Package": ["0805 / Larger", "0402", "0201", "01005"],
    "Barrier Score": [1, 2, 3, 4],
    "Strategic Value Score": [1, 2, 3, 4],
})

capacity_df = pd.DataFrame({
    "Node": ["Japan (Mother-Factories)", "China (Scale Centers)", "ASEAN (Vietnam/Philippines)"],
    "Barrier": [5, 2, 3],
    "Risk": [3, 5, 4],
    "Reward": [5, 3, 4],
})

win_loss_df = pd.DataFrame({
    "Vector": ["Ultra-Miniature RF (01005)", "Automotive Niche (PoC)", "Domestic China Scale", "Advanced Material IP"],
    "Outcome Score": [2, 5, 1, 5],
    "Label": ["Contested / Partial Loss", "Clear Win Zone", "Structural Loss Zone", "Clear Win Zone"],
})

# -----------------------------
# SESSION STATE
# -----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "visitor_name" not in st.session_state:
    st.session_state.visitor_name = ""
if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "Overview"

# -----------------------------
# CSS
# -----------------------------
def inject_css(login_mode: bool = False) -> None:
    sidebar_login_hide = "section[data-testid='stSidebar'] {display:none !important;}" if login_mode else ""
    st.markdown(
        f"""
        <style>
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
            button[kind="secondary"] {{display:none;}}
            [data-testid="stToolbar"] {{display:none !important;}}
            [data-testid="stDecoration"] {{display:none !important;}}
            .stDeployButton {{display:none !important;}}
            button[data-testid="baseButton-headerNoPadding"] {{display:none !important;}}
            {sidebar_login_hide}

            .stApp {{
                background:
                    radial-gradient(circle at top left, rgba(232,199,213,0.18), transparent 28%),
                    linear-gradient(180deg, #FBF8F9 0%, #F5F1F3 100%);
            }}

            html, body, [class*="css"] {{
                font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                color: {INK};
            }}

            section[data-testid="stSidebar"] {{
                background: linear-gradient(180deg, #2E0A18 0%, #431024 100%);
                border-right: 1px solid rgba(255,255,255,0.07);
            }}

            section[data-testid="stSidebar"] * {{
                color: #FFF7FA !important;
            }}

            [data-testid="stSidebarNav"] {{
                display:none !important;
            }}

            div[data-baseweb="select"] > div,
            div[data-baseweb="input"] > div {{
                border-radius: 14px !important;
            }}

            .main-shell {{
                max-width: 1360px;
                margin: 0 auto;
                padding-bottom: 2rem;
            }}

            .hero-card {{
                position: relative;
                overflow: hidden;
                background: linear-gradient(135deg, rgba(91,15,46,1) 0%, rgba(67,16,36,1) 72%);
                border-radius: 28px;
                padding: 34px 38px;
                color: white;
                box-shadow: 0 18px 40px rgba(91,15,46,0.22);
                border: 1px solid rgba(255,255,255,0.08);
                margin-bottom: 18px;
            }}

            .hero-card:before {{
                content: "";
                position: absolute;
                right: -120px;
                top: -80px;
                width: 320px;
                height: 320px;
                background: radial-gradient(circle, rgba(255,255,255,0.10) 0%, transparent 65%);
            }}

            .hero-kicker {{
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 0.16em;
                text-transform: uppercase;
                color: #F6DDE6;
                margin-bottom: 12px;
            }}

            .hero-title {{
                font-size: 2.8rem;
                line-height: 1.14;
                font-weight: 800;
                margin-bottom: 12px;
            }}

            .hero-subtitle {{
                font-size: 1.15rem;
                color: #F8E8EF;
                max-width: 780px;
            }}

            .metric-card {{
                background: rgba(255,255,255,0.96);
                border: 1px solid {BORDER};
                border-radius: 20px;
                padding: 18px 18px 16px 18px;
                min-height: 150px;
                box-shadow: 0 10px 26px rgba(15,23,42,0.06);
            }}

            .metric-label {{
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                color: #64748B;
                font-weight: 800;
                margin-bottom: 10px;
            }}

            .metric-value {{
                font-size: 1.95rem;
                line-height: 1.1;
                color: {BURGUNDY};
                font-weight: 800;
                margin-bottom: 8px;
            }}

            .metric-note {{
                font-size: 14px;
                line-height: 1.55;
                color: #6B7280;
            }}

            .sidebar-brand {{
                background: rgba(255,255,255,0.06);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 18px;
                padding: 16px 16px 14px 16px;
                margin-bottom: 10px;
                box-shadow: 0 10px 24px rgba(0,0,0,0.18);
            }}

            .sidebar-kicker {{
                font-size: 11px;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                color: #E9C7D5 !important;
                margin-bottom: 6px;
            }}

            .sidebar-title {{
                font-size: 20px;
                line-height: 1.25;
                font-weight: 800;
                margin-bottom: 6px;
            }}

            .sidebar-sub {{
                font-size: 12px;
                color: #F1DDE5 !important;
            }}

            .sidebar-user {{
                background: rgba(255,255,255,0.05);
                border-radius: 14px;
                padding: 12px 14px;
                border: 1px solid rgba(255,255,255,0.06);
                margin: 10px 0 14px;
                color: #FDEEF5;
                font-size: 13px;
            }}

            .section-title {{
                font-size: 1.32rem;
                font-weight: 800;
                color: {INK};
                margin: 0 0 0.35rem 0;
            }}

            .section-subtitle {{
                color: {SLATE};
                font-size: 0.96rem;
                margin-bottom: 1rem;
            }}

            .report-shell {{
                background: rgba(255,255,255,0.96);
                border: 1px solid {BORDER};
                border-radius: 24px;
                box-shadow: 0 14px 32px rgba(15,23,42,0.06);
                overflow: hidden;
                margin-top: 16px;
            }}

            .report-banner {{
                background: linear-gradient(135deg, #FFF6F9 0%, #FAEDF2 100%);
                border-bottom: 1px solid #EED7E1;
                padding: 18px 26px;
            }}

            .report-title {{
                font-size: 1.6rem;
                font-weight: 800;
                color: {INK};
            }}

            .report-card {{
                padding: 26px 30px 30px 30px;
            }}

            .chapter-content h1 {{
                font-size: 2.15rem;
                font-weight: 800;
                color: #0F172A;
                margin-top: 0;
                margin-bottom: 1.5rem;
                border-bottom: 2px solid #E2E8F0;
                padding-bottom: 0.55rem;
            }}

            .chapter-content h2 {{
                font-size: 1.5rem;
                font-weight: 700;
                color: #1E293B;
                margin-top: 2rem;
                margin-bottom: 1rem;
            }}

            .chapter-content h3 {{
                font-size: 1.2rem;
                font-weight: 700;
                color: #334155;
                margin-top: 1.5rem;
                margin-bottom: 0.75rem;
            }}

            .chapter-content p {{
                margin-bottom: 1.25rem;
                line-height: 1.8;
                color: #334155;
                text-align: justify;
                font-size: 0.99rem;
            }}

            .chapter-content table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1.5rem 0;
                background-color: #ffffff;
                box-shadow: 0 1px 3px rgba(0,0,0,0.08);
                border-radius: 0.6rem;
                overflow: hidden;
                border: 1px solid #E2E8F0;
            }}

            .chapter-content th {{
                background: linear-gradient(180deg, #5B0F2E 0%, #431024 100%);
                color: #ffffff;
                font-weight: 700;
                text-align: left;
                padding: 0.85rem 1rem;
                border-bottom: 2px solid #6E2341;
                font-size: 0.88rem;
            }}

            .chapter-content td {{
                padding: 0.8rem 1rem;
                border-bottom: 1px solid #E2E8F0;
                color: #334155;
                font-size: 0.88rem;
                vertical-align: top;
            }}

            .chapter-content tr:last-child td {{
                border-bottom: none;
            }}

            .chapter-content tr:hover td {{
                background-color: #FBF5F7;
            }}

            .insight-highlight {{
                background-color: #FAF2F5;
                border-left: 4px solid #8A1E4F;
                padding: 1rem 1.25rem;
                margin: 1.5rem 0;
                font-style: italic;
                color: #7A163F;
                font-weight: 600;
                border-radius: 0 0.5rem 0.5rem 0;
            }}

            .post-table-insight {{
                background-color: #FCFAFB;
                border: 1px solid #E8DCE2;
                padding: 1rem;
                margin-top: -1rem;
                margin-bottom: 1.5rem;
                font-size: 0.88rem;
                color: #5B4B54;
                border-radius: 0 0 0.5rem 0.5rem;
            }}

            .small-callout {{
                background: rgba(255,255,255,0.96);
                border: 1px solid {BORDER};
                border-radius: 18px;
                padding: 16px 18px;
                box-shadow: 0 10px 26px rgba(15,23,42,0.05);
            }}

            .chapter-note {{
                background: #FFF8FB;
                border: 1px solid #F0D6E1;
                border-radius: 16px;
                padding: 14px 16px;
                color: #6B213E;
                font-size: 14px;
                margin-bottom: 14px;
            }}

            [data-testid="stForm"] {{
                border: none !important;
                padding: 0 !important;
            }}

            [data-testid="stTextInput"] label,
            [data-testid="stRadio"] label {{
                font-weight: 700 !important;
                color: {INK} !important;
            }}

            .stButton > button {{
                background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_DARK} 100%);
                color: white;
                border: none;
                border-radius: 14px;
                padding: 0.7rem 1rem;
                font-weight: 700;
                box-shadow: 0 10px 20px rgba(91,15,46,0.18);
            }}

            .stButton > button:hover {{
                filter: brightness(1.04);
                transform: translateY(-1px);
            }}

            @media (max-width: 768px) {{
                .report-card {{
                    padding: 20px 18px 22px 18px;
                }}
                .hero-card {{
                    padding: 26px 22px;
                    border-radius: 22px;
                }}
                .metric-value {{
                    font-size: 1.65rem;
                }}
            }}
        </style>
        <meta http-equiv="refresh" content="300">
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# HELPERS
# -----------------------------
def metric_card(label: str, value: str, note: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def section_intro(title: str, subtitle: str) -> None:
    st.markdown(
        f'<div class="section-title">{title}</div><div class="section-subtitle">{subtitle}</div>',
        unsafe_allow_html=True,
    )

def style_plot(fig: go.Figure, title: str, height: int = 360) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0, xanchor="left", font=dict(size=18, color=INK)),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Inter, sans-serif", color=SLATE),
        margin=dict(l=18, r=18, t=58, b=18),
        height=height,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        hoverlabel=dict(bgcolor="white", font_color=INK),
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor="rgba(148,163,184,0.18)", zeroline=False)
    return fig

def safe_get_html(title: str) -> str:
    return CHAPTERS.get(title, f"""
    <div class="chapter-content">
        <h1>{title}</h1>
        <p>No content found for this chapter.</p>
    </div>
    """)

def insert_chart_anchor(title: str, html_content: str) -> str:
    """
    Insert a single safe anchor into selected chapters.
    If the anchor cannot be inserted cleanly, the function returns original HTML.
    """
    replacements = {
        "1. ": "</p>\n<table>",
        "3. ": "</div>\n<p>",
        "4. ": "</div>\n<p>",
        "7. ": "</div>\n<p>",
        "18. ": "</div>\n<p>",
    }

    for prefix, marker in replacements.items():
        if title.startswith(prefix) and marker in html_content and CHART_ANCHOR not in html_content:
            return html_content.replace(marker, f"\n{CHART_ANCHOR}\n{marker}", 1)

    return html_content

# -----------------------------
# INLINE PLOTLY CHARTS
# -----------------------------
def market_revenue_chart():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["2025", "2030", "2035"],
        y=[1446.7, 1727.5, 2115.3],
        marker_color=BURGUNDY,
        text=["1,446.7", "1,727.5", "2,115.3"],
        textposition="outside",
        name="Revenue"
    ))
    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "Market Expansion ($Mn)", 330)
    st.plotly_chart(fig, use_container_width=True)

def market_volume_chart():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["2025", "2030", "2035"],
        y=[85.4, 112.5, 146.4],
        marker_color=BURGUNDY_LIGHT,
        text=["85.4", "112.5", "146.4"],
        textposition="outside",
        name="Volume"
    ))
    fig.update_yaxes(title_text="Volume (Bn Units)")
    style_plot(fig, "Volume Scaling (Bn Units)", 330)
    st.plotly_chart(fig, use_container_width=True)

def tam_combo_chart():
    col1, col2 = st.columns(2)

    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=["2025", "2030", "2035"],
            y=[5108.5, 6518.0, 8389.8],
            marker_color=BURGUNDY,
            text=["5,108.5", "6,518.0", "8,389.8"],
            textposition="outside",
            name="Device Anchors"
        ))
        fig1.update_yaxes(title_text="Device Anchors (Mn)")
        style_plot(fig1, "Total Device Anchors", 330)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=["2025", "2030", "2035"],
            y=[16.7, 17.2, 17.4],
            mode="lines+markers+text",
            text=["16.7", "17.2", "17.4"],
            textposition="top center",
            line=dict(color=BURGUNDY_LIGHT, width=4),
            marker=dict(size=9, color=BURGUNDY_LIGHT),
            fill="tozeroy",
            fillcolor="rgba(122,22,63,0.08)",
            name="Components per Device"
        ))
        fig2.update_yaxes(title_text="Components per Device")
        style_plot(fig2, "Density Metrics", 330)
        st.plotly_chart(fig2, use_container_width=True)

def segment_stacked_chart():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["2025", "2030", "2035"], y=[839, 973, 1143],
        name="RF", marker_color=BURGUNDY
    ))
    fig.add_trace(go.Bar(
        x=["2025", "2030", "2035"], y=[474, 560, 672],
        name="Ferrite", marker_color="#7A1C3A"
    ))
    fig.add_trace(go.Bar(
        x=["2025", "2030", "2035"], y=[132, 193, 299],
        name="Automotive", marker_color="#B07A92"
    ))
    fig.update_layout(barmode="stack")
    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "Segment Evolution ($Mn)", 360)
    st.plotly_chart(fig, use_container_width=True)

def pricing_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=["2025", "2030", "2035"], y=[0.0220, 0.0215, 0.0210],
        mode="lines+markers", name="RF",
        line=dict(color=BURGUNDY, width=3),
        marker=dict(size=8, color=BURGUNDY)
    ))
    fig.add_trace(go.Scatter(
        x=["2025", "2030", "2035"], y=[0.0350, 0.0340, 0.0330],
        mode="lines+markers", name="Auto",
        line=dict(color=BURGUNDY_LIGHT, width=3),
        marker=dict(size=8, color=BURGUNDY_LIGHT)
    ))
    fig.update_yaxes(title_text="ASP ($)")
    style_plot(fig, "Pricing Erosion & Premium Resistance", 360)
    st.plotly_chart(fig, use_container_width=True)

def scenario_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=["2025", "2030", "2035"], y=[1578.90, 1885.43, 2308.58],
        mode="lines+markers", name="Upside",
        line=dict(color=BURGUNDY_LIGHT, width=3, dash="dash")
    ))
    fig.add_trace(go.Scatter(
        x=["2025", "2030", "2035"], y=[1446.68, 1727.53, 2115.25],
        mode="lines+markers", name="Base",
        line=dict(color=BURGUNDY, width=4)
    ))
    fig.add_trace(go.Scatter(
        x=["2025", "2030", "2035"], y=[1305.05, 1558.41, 1908.16],
        mode="lines+markers", name="Downside",
        line=dict(color="#A4456F", width=3, dash="dot")
    ))
    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "Strategic Scenarios ($Mn)", 360)
    st.plotly_chart(fig, use_container_width=True)

def render_inline_chart(title: str) -> None:
    if title.startswith("1. "):
        col1, col2 = st.columns(2)
        with col1:
            market_revenue_chart()
        with col2:
            market_volume_chart()
    elif title.startswith("3. "):
        tam_combo_chart()
    elif title.startswith("4. "):
        segment_stacked_chart()
    elif title.startswith("7. "):
        pricing_chart()
    elif title.startswith("18. "):
        scenario_chart()

def render_hero() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-kicker">Boardroom Preview Dashboard</div>
            <div class="hero-title">Global Multilayer Inductor Market (2025–2035)</div>
            <div class="hero-subtitle">Demand expansion, RF complexity, automotive qualification, and portfolio strategy — translated into a dynamic executive dashboard for TDK.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_overview() -> None:
    render_hero()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Market Revenue 2035", QUICK_METRICS["Market Revenue 2035"], "Global multilayer inductor market")
    with c2:
        metric_card("Global CAGR", QUICK_METRICS["Global CAGR"], "2025–2035 base case")
    with c3:
        metric_card("TDK 2025 Proxied", QUICK_METRICS["TDK 2025 Proxied"], "Illustrative revenue position")
    with c4:
        metric_card("Premium Growth Vector", QUICK_METRICS["Premium Growth Vector"], "High-barrier value pool")

    st.markdown("")
    tab1, tab2, tab3, tab4 = st.tabs(["Market trajectory", "Value pools", "Regional architecture", "Competition & scenarios"])

    with tab1:
        section_intro("Trajectory and pricing", "The overview layer concentrates the most decision-critical variables: revenue, volume, and ASP compression.")
        col_a, col_b = st.columns([1.35, 1])
        with col_a:
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Scatter(
                x=market_df["Year"], y=market_df["Revenue"],
                mode="lines+markers",
                name="Revenue ($Mn)",
                line=dict(color=BURGUNDY, width=4),
                marker=dict(size=10, color=BURGUNDY)
            ), secondary_y=False)
            fig.add_trace(go.Bar(
                x=market_df["Year"], y=market_df["Volume"],
                name="Volume (Bn units)",
                marker_color="#D7B2C0",
                opacity=0.78
            ), secondary_y=True)
            fig.update_yaxes(title_text="Revenue ($Mn)", secondary_y=False)
            fig.update_yaxes(title_text="Volume (Bn units)", secondary_y=True)
            style_plot(fig, "Revenue expansion vs. volume scale", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            asp_fig = go.Figure()
            asp_fig.add_trace(go.Scatter(
                x=market_df["Year"], y=market_df["ASP"],
                mode="lines+markers+text",
                text=[f"${x:.4f}" for x in market_df["ASP"]],
                textposition="top center",
                line=dict(color=BURGUNDY_LIGHT, width=4),
                marker=dict(size=10, color=BURGUNDY_LIGHT),
                fill="tozeroy",
                fillcolor="rgba(122,22,63,0.08)",
                name="ASP ($/unit)"
            ))
            asp_fig.update_yaxes(title_text="ASP ($/unit)")
            style_plot(asp_fig, "Blended ASP compression", 380)
            st.plotly_chart(asp_fig, use_container_width=True)

    with tab2:
        section_intro("Segment structure and device pull", "Value creation is migrating toward automotive-qualified components even while RF maintains scale leadership.")
        col_a, col_b = st.columns([1.25, 1])
        with col_a:
            melt = segment_df.melt(id_vars="Segment", var_name="Year", value_name="Revenue")
            fig = px.bar(
                melt, x="Year", y="Revenue", color="Segment", barmode="group",
                color_discrete_sequence=[BURGUNDY, "#B07A92", "#E7C7D5"]
            )
            style_plot(fig, "Segment revenue by year", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            fig = go.Figure(data=[go.Pie(
                labels=["RF", "Compact Ferrite / NFC", "Automotive-Qualified"],
                values=[54.0, 31.7, 14.1],
                hole=0.62,
                marker=dict(colors=[BURGUNDY, "#B07A92", "#E7C7D5"]),
                sort=False
            )])
            fig.update_traces(textinfo="label+percent")
            style_plot(fig, "2035 mix shift toward automotive", 380)
            st.plotly_chart(fig, use_container_width=True)

        device_melt = device_df.melt(id_vars="Device", value_vars=["2025", "2035"], var_name="Year", value_name="Volume")
        fig = px.bar(
            device_melt,
            x="Device",
            y="Volume",
            color="Year",
            barmode="group",
            color_discrete_sequence=[BURGUNDY, "#D7B2C0"]
        )
        fig.update_layout(xaxis_tickangle=-18)
        style_plot(fig, "Device-level demand engine: 2025 vs. 2035", 390)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        section_intro("Regional architecture", "Asia remains the volume center of gravity while Europe and North America protect premium automotive value pools.")
        col_a, col_b = st.columns([1.1, 1.2])
        with col_a:
            region_rollup = pd.DataFrame({
                "Region": ["North America", "Europe", "Asia Pacific + Japan"],
                "2025": [north_america_df["2025"].sum(), europe_df["2025"].sum(), apac_df["2025"].sum()],
                "2035": [north_america_df["2035"].sum(), europe_df["2035"].sum(), apac_df["2035"].sum()],
            })
            melt = region_rollup.melt(id_vars="Region", var_name="Year", value_name="Revenue")
            fig = px.bar(
                melt, x="Region", y="Revenue", color="Year", barmode="group",
                color_discrete_sequence=[BURGUNDY, "#D7B2C0"]
            )
            style_plot(fig, "Regional value pools: 2025 vs. 2035", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            country_2035 = pd.concat([
                north_america_df.assign(Group="North America"),
                europe_df.assign(Group="Europe"),
                apac_df.assign(Group="Asia Pacific + Japan")
            ], ignore_index=True).sort_values("2035", ascending=True)
            fig = px.bar(
                country_2035,
                x="2035",
                y="Region",
                color="Group",
                orientation="h",
                color_discrete_sequence=[BURGUNDY, "#B07A92", "#E7C7D5"]
            )
            style_plot(fig, "2035 country / sub-region stack", 380)
            st.plotly_chart(fig, use_container_width=True)

    with tab4:
        section_intro("Competitive positioning and scenario stress-testing", "Competitive share is anonymized, while the scenario view highlights upside and downside sensitivity.")
        col_a, col_b = st.columns([1.05, 1.15])
        with col_a:
            melt = competitive_df.melt(id_vars="Competitor", var_name="Year", value_name="Share")
            fig = px.bar(
                melt, x="Competitor", y="Share", color="Year", barmode="group",
                color_discrete_sequence=[BURGUNDY, "#D7B2C0"]
            )
            style_plot(fig, "Anonymized market share view", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            fig = go.Figure()
            for name, color in [
                ("Base Case Reality", BURGUNDY),
                ("Optimized Upside", "#A4456F"),
                ("Constrained Downside", "#D8B5C3"),
            ]:
                fig.add_trace(go.Scatter(
                    x=scenario_df["Year"], y=scenario_df[name],
                    mode="lines+markers", name=name,
                    line=dict(width=4, color=color),
                    marker=dict(size=9, color=color)
                ))
            fig.update_yaxes(title_text="Revenue ($Mn)")
            style_plot(fig, "Scenario sensitivity through 2035", 380)
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("")
    st.markdown(
        """
        <div class="small-callout">
            <div class="section-title" style="margin-bottom:8px;">Executive interpretation</div>
            <div class="section-subtitle" style="margin-bottom:0;">
                The dashboard confirms a structural market rotation: RF remains the scale engine, automotive becomes the premium margin engine, and Asia remains the manufacturing gravity center. The strategic implication is not to chase all volume equally — it is to defend scale where necessary while concentrating investment in zero-defect, miniaturized, automotive-qualified architectures.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_prev_next(options: list[str], current: str) -> None:
    idx = options.index(current)
    col1, col2 = st.columns([1, 1])

    with col1:
        if idx > 0:
            if st.button("⬅ Previous"):
                st.session_state["nav_choice"] = options[idx - 1]
                st.rerun()

    with col2:
        if idx < len(options) - 1:
            if st.button("Next ➡"):
                st.session_state["nav_choice"] = options[idx + 1]
                st.rerun()

def render_chapter_page(title: str, nav_options: list[str]) -> None:
    st.markdown(
        f"""
        <div class="report-shell">
            <div class="report-banner">
                <div class="report-title">{title}</div>
            </div>
            <div class="report-card">
        """,
        unsafe_allow_html=True,
    )

    html_content = safe_get_html(title)
    html_content = insert_chart_anchor(title, html_content)

    if CHART_ANCHOR in html_content:
        parts = html_content.split(CHART_ANCHOR, 1)
        st.markdown(parts[0], unsafe_allow_html=True)
        render_inline_chart(title)
        if len(parts) > 1 and parts[1].strip():
            st.markdown(parts[1], unsafe_allow_html=True)
    else:
        st.markdown(html_content, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
    render_prev_next(nav_options, title)

    st.markdown("""
    ---
    **Confidential & Proprietary** © 2026 Strategic Market Research  

    To access the full report:  
    📩 info@strategicmarketresearch.com
    """)

def render_login() -> None:
    inject_css(login_mode=True)
    _, col, _ = st.columns([1, 1.2, 1])

    with col:
        st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("""
                <h2 style='text-align: center; color: #5B0F2E; padding-bottom: 15px;'>
                    SMR BOARDROOM ACCESS
                </h2>
            """, unsafe_allow_html=True)

            name = st.text_input("Name", placeholder="Enter your name")
            password = st.text_input("Password", type="password", placeholder="Enter password")

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button("Enter Dashboard", type="primary", use_container_width=True):
                if password == PRIMARY_PASSWORD:
                    st.session_state.authenticated = True
                    st.session_state.visitor_name = name.strip() or "Guest"
                    st.session_state.nav_choice = "Overview"
                    st.rerun()
                else:
                    st.error("Incorrect password")

# -----------------------------
# APP
# -----------------------------
if not st.session_state.authenticated:
    render_login()
    st.stop()

inject_css(login_mode=False)

nav_options = ["Overview"] + list(CHAPTERS.keys())

st.sidebar.markdown(
    f"""
    <div class="sidebar-brand">
        <div class="sidebar-kicker">Strategic Market Research</div>
        <div class="sidebar-title">Global Multilayer Inductor Market</div>
        <div class="sidebar-sub">Client: {CLIENT_NAME}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f"""
    <div class="sidebar-user">
        Viewing as <strong>{st.session_state.visitor_name}</strong><br>
        Premium preview mode · Tier 3 dashboard
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.radio(
    "Navigate",
    nav_options,
    key="nav_choice",
    label_visibility="collapsed",
)

st.sidebar.caption("Confidential & Proprietary")
st.sidebar.caption("© 2026 Strategic Market Research")

if st.sidebar.button("Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.visitor_name = ""
    st.session_state.nav_choice = "Overview"
    st.rerun()

st.markdown('<div class="main-shell">', unsafe_allow_html=True)

if st.session_state.nav_choice == "Overview":
    render_overview()
else:
    render_chapter_page(st.session_state.nav_choice, nav_options)

st.markdown('</div>', unsafe_allow_html=True)
