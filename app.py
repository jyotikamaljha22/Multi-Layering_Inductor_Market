import os
import csv
import base64
from datetime import datetime, timezone
from pathlib import Path
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
# THEME COLORS & LOGO LOGIC
# =========================
BURGUNDY = "#4A0C25" 
BURGUNDY_DARK = "#2D0716"
GOLD = "#C49A23"
SLATE = "#475569"

@st.cache_data
def load_logo_base64() -> str | None:
    candidates = [
        Path("smrlogonew.svg"), 
        Path(__file__).with_name("smrlogonew.svg"), 
        Path.cwd() / "smrlogonew.svg"
    ]
    for path in candidates:
        if path.exists():
            try: return base64.b64encode(path.read_bytes()).decode("utf-8")
            except Exception: pass
    return None

LOGO_B64 = load_logo_base64()

# =========================
# CSS HIDING & MAIN UI POLISH
# =========================
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}

    /* UI ERADICATION */
    [data-testid="stSidebar"] {{ display: none !important; }}
    [data-testid="collapsedControl"] {{ display: none !important; }}
    [data-testid="stToolbar"] {{ display: none !important; }}
    header[data-testid="stHeader"] {{ background: transparent !important; box-shadow: none !important; }}
    footer {{ display: none !important; }}
    .viewerBadge_container, #viewerBadge_container {{ display: none !important; }}
    
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }}

    /* LOGIN GATEWAY STYLING */
    div[data-baseweb="input"] {{
        background-color: #ffffff !important;
        border-radius: 8px !important;
    }}
    .stTextInput input {{
        border-radius: 8px !important; 
        border: 1px solid #cbd5e1 !important;
        padding: 12px 14px !important; 
        background-color: #ffffff !important; 
        color: #1A1A1A !important;
        -webkit-text-fill-color: #1A1A1A !important;
    }}
    .stTextInput input:focus {{
        border-color: {GOLD} !important;
        box-shadow: 0 0 0 2px rgba(196, 154, 35, 0.2) !important;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_DARK} 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 12px 24px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 15px rgba(74, 12, 37, 0.25) !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(74, 12, 37, 0.4) !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- JAILBREAK SCRIPT ---
components.html(
    """<script>setTimeout(function() {var e = window.parent.document.querySelector('[data-testid="collapsedControl"]'); if(e) e.click();}, 100);</script>""",
    height=0, width=0
)

# ----------------------------
# ACCESS CONTROL
# ----------------------------
def check_access():
    expected_password = str(st.secrets.get("ACCESS_CODE", "SMR2026")).strip()
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if st.session_state.authenticated:
        return True

    st.markdown("<div style='margin-top: 10vh;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        if LOGO_B64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:65px; margin-bottom:20px;" /></div>', unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='text-align:center; color:{BURGUNDY}; font-weight:800; font-size:2.2rem; margin-bottom:0;'>Strategic Market Research</h1>", unsafe_allow_html=True)
            
        st.markdown(f"<p style='text-align:center; color:{GOLD}; font-weight:800; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:30px; font-size: 0.9rem;'>TDK Corporation Executive Advisory</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            st.markdown(f"<h3 style='color:#1e293b; font-weight:800; margin-bottom:20px; text-align:center; font-size: 1.4rem;'>🔐 Secure Authentication</h3>", unsafe_allow_html=True)
            name = st.text_input("Executive Name*")
            email = st.text_input("Corporate Email*")
            password = st.text_input("Access Code*", type="password")
            st.markdown("<br>", unsafe_allow_html=True)
            enter = st.form_submit_button("Enter Boardroom", use_container_width=True)

    if enter:
        if not name or not email or not password:
            with col2: st.warning("⚠️ All fields required.")
        elif password.strip() != expected_password:
            with col2: st.error("❌ Invalid Code.")
        else:
            st.session_state.authenticated = True
            st.session_state.viewer_name = name.strip()
            st.rerun()
    st.stop()

check_access()

# --- TOP BAR FOR LOGOUT ---
col1, col2, col3 = st.columns([1, 5, 1])
with col3:
    st.markdown(f"<div style='text-align:right; font-size:0.8rem; font-weight:600; color:{SLATE}; margin-bottom:4px; margin-top:8px;'>Verified: <span style='color:{BURGUNDY}'>{st.session_state.viewer_name}</span></div>", unsafe_allow_html=True)
    if st.button("🔒 End Session", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ----------------------------
# HTML DASHBOARD CONTENT (FULL 20 CHAPTERS)
# ----------------------------
html_logo = f'<img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:32px; width:auto; filter: brightness(0) invert(1);" />' if LOGO_B64 else ""

RAW_HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Multilayer Inductor Market (2025–2035) | TDK Advisory</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #f8fafc; }
        .chapter-content { display: none; animation: fadeIn 0.4s ease-in-out; }
        .chapter-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 1.5rem 0; background-color: #ffffff; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; }
        th { background-color: #4A0C25; color: #ffffff; font-weight: 700; text-align: left; padding: 1rem; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }
        td { padding: 1rem; border-bottom: 1px solid #f1f5f9; color: #334155; font-size: 0.875rem; vertical-align: top; }
        tr:hover td { background-color: #fafafa; }
        
        p { margin-bottom: 1.5rem; line-height: 1.8; color: #475569; text-align: justify; font-size: 1rem; }
        h1 { font-size: 2.2rem; font-weight: 800; color: #1e293b; margin-bottom: 1.5rem; border-bottom: 4px solid #C49A23; padding-bottom: 0.5rem; letter-spacing: -0.02em; }
        h2 { font-size: 1.5rem; font-weight: 700; color: #4A0C25; margin-top: 2rem; margin-bottom: 1rem; }
        
        .frost-lock { filter: blur(8px); opacity: 0.2; pointer-events: none; user-select: none; }
        .teaser-box { background: #fffbeb; border: 1px solid #fde68a; padding: 1.5rem; border-radius: 8px; color: #92400e; font-weight: 600; font-size: 0.9rem; margin-bottom: 1.5rem; text-align: center; }

        .insight-highlight { background: linear-gradient(135deg, #fdfcfd 0%, #fff 100%); border-left: 5px solid #C49A23; padding: 1.5rem; margin: 2rem 0; font-style: italic; color: #4A0C25; font-weight: 600; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
        
        .sidebar { background-color: #2D0716; }
        .nav-item { cursor: pointer; transition: all 0.2s; color: #9ca3af; border-left: 4px solid transparent; }
        .nav-item:hover { background-color: rgba(255,255,255,0.05); color: #ffffff; }
        .nav-item.active { background-color: rgba(255,255,255,0.1); color: #C49A23; font-weight: 700; border-left: 4px solid #C49A23; }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: rgba(196,154,35,0.4); border-radius: 10px; }
    </style>
</head>
<body class="flex h-screen overflow-hidden">

    <aside class="w-80 sidebar text-slate-300 flex flex-col h-full overflow-y-auto shrink-0 shadow-2xl z-20">
        <div class="p-8 border-b border-white/10 sticky top-0 sidebar">
            <div class="mb-4">__LOGO_PLACEHOLDER__</div>
            <div class="text-xs font-bold tracking-widest text-[#C49A23] uppercase mb-1">Strategic Market Research</div>
            <h2 class="text-xl font-extrabold text-white leading-tight">Multilayer Inductor <br>Master Advisory 2035</h2>
            <div class="text-xs text-slate-400 mt-2 font-medium">Internal TDK Corporate Briefing</div>
        </div>
        <nav class="flex-1 py-4" id="sidebar-nav"></nav>
        <div class="p-6 border-t border-white/10 text-[10px] text-slate-500 uppercase tracking-widest bg-black/20">
            &copy; 2026 SMR Group • Confidential
        </div>
    </aside>

    <main class="flex-1 overflow-y-auto bg-slate-50 relative p-8 md:p-12 lg:p-20 scroll-smooth" id="main-content">
        
        <article id="ch1" class="chapter-content active max-w-5xl mx-auto">
            <h1>1. Executive Summary & Strategic Objective</h1>
            <p>The global multilayer inductor market operates as a foundational pillar within modern electronic architecture, driven by the absolute necessity for precision radio frequency matching and robust power regulation. Demand is structurally tied to the proliferation of compact, high-density electronic assemblies across advanced mobile, industrial, and automotive platforms. The underlying economic landscape heavily rewards extreme miniaturization and stringent environmental qualification over pure production scale.</p>
            <p>The trajectory of the multilayer inductor sector is fundamentally defined by the transition from volumetric consumer electronics growth toward value-dense automotive and industrial applications. Historically, market expansion relied on the sheer unit scale of smartphone and generic computing device production, which offered reliable but low-margin revenue streams. Contemporary market dynamics, however, indicate that raw unit volumes no longer correlate linearly with revenue generation, as advanced applications require highly specialized, premium-priced components. Consequently, manufacturers that successfully pivot their portfolios toward stringent qualification standards secure disproportionate shares of the expanding industry profit pool.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 ($Mn)</th><th>2035 ($Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>RF / High-Frequency</td><td>$839.12</td><td>$1,143.43</td><td>3.14%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>$474.81</td><td>$672.22</td><td>3.54%</td></tr>
                    <tr><td>Automotive-Qualified</td><td>$132.75</td><td>$299.60</td><td>8.48%</td></tr>
                </tbody>
            </table>
            <div class="insight-highlight">Value creation in the multilayer inductor market is rapidly decoupling from pure unit volumes, heavily favoring automotive qualification and ultra-high-frequency capabilities as the ultimate drivers of corporate profitability.</div>
        </article>

        <article id="ch2" class="chapter-content max-w-5xl mx-auto">
            <h1>2. Market Core: Global Size, Volume & Trajectory</h1>
            <p>The global multilayer inductor market represents a highly concentrated economic ecosystem where total value is governed by the intersection of aggregate device shipments and individual component complexity. Demand is perpetually driven by the necessity to route complex signals through increasingly dense, miniaturized printed circuit boards within mobility and edge-computing hardware. Sustained revenue expansion therefore requires continuous technological iteration to satisfy the severe spatial limitations and thermal constraints of contemporary hardware architectures.</p>
            <p>The absolute scale is anchored by an immense volume of individual component shipments, which are projected to expand significantly over the forecast horizon. This volume expansion is driven by the increasing electronic content per device across virtually all major hardware categories, successfully counterbalancing the plateauing shipment growth of mature consumer devices like smartphones. The manufacturing base faces immense pressure to scale physical output while strictly maintaining the precise electromagnetic characteristics required by telecommunications and automotive end-users, leaving no margin for quality degradation.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 (Bn units)</th><th>2030 (Bn units)</th><th>2035 (Bn units)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>RF / High-Frequency</td><td>38.14</td><td>45.29</td><td>54.45</td><td>3.62%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>35.17</td><td>43.07</td><td>53.78</td><td>4.33%</td></tr>
                    <tr><td>Automotive-Qualified</td><td>3.69</td><td>5.24</td><td>7.88</td><td>7.88%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch3" class="chapter-content max-w-5xl mx-auto">
            <h1>3. Pricing & Value Dynamics</h1>
            <p>Segment economics within the multilayer inductor industry are strictly dictated by the average selling price, which remains highly sensitive to the specific material composition, precision, and operational rating of the manufactured component. The financial viability of manufacturing operations relies heavily on actively protecting these price points against the natural deflationary pressures inherent in mature electronic component supply chains. Maintaining robust operating margins requires relentless innovation in proprietary sintering and layering techniques to continually justify premium pricing architectures to procurement teams.</p>
            <p>Pricing architectures across the industry reveal a distinct, rigid hierarchy based entirely on application criticality and manufacturing difficulty. Automotive-qualified inductors command the highest average selling price due to the exhaustive testing protocols, extended thermal warranties, and stringent reliability standards required for integration into safety-critical vehicle systems. Radio frequency inductors occupy a highly strategic middle ground within the pricing hierarchy, where extreme miniaturization and demanding high-Q performance requirements provide a formidable defensive moat.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 ASP ($/unit)</th><th>2035 ASP ($/unit)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Automotive-Qualified</td><td>$0.0360</td><td>$0.0380</td><td>0.54%</td></tr>
                    <tr><td>RF / High-Frequency</td><td>$0.0220</td><td>$0.0210</td><td>-0.46%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>$0.0135</td><td>$0.0125</td><td>-0.76%</td></tr>
                </tbody>
            </table>
            <div class="insight-highlight">Premium component pricing is sustained strictly by thermal reliability thresholds and structural qualification parameters, creating a formidable economic moat against high-volume consumer commoditization.</div>
        </article>

        <article id="ch4" class="chapter-content max-w-5xl mx-auto">
            <h1>4. Demand Engine: Device-Level Modeling (Smartphones & Wearables)</h1>
            <p>Smartphones and wearable devices constitute the absolute baseline of global multilayer inductor consumption, characterized by massive aggregate device shipments and extreme internal spatial constraints. The primary economic driver for this segment is the continuous, uncompromising requirement for advanced impedance matching and signal filtering within increasingly crowded and thermally limited printed circuit boards. Commercial success in this arena demands that manufacturers master ultra-miniaturization while reliably delivering billions of functionally identical components without interruption.</p>
            <p>The smartphone ecosystem remains the largest single consumer of multilayer inductors, despite a well-documented maturation in the underlying global device shipment growth rates. The vital metric sustaining component demand is the content-per-device multiple, which continues to expand aggressively as original equipment manufacturers integrate complex 5G radio frequency front-ends and sophisticated power management integrated circuits into every handset.</p>
            <div class="teaser-box">🔒 15-Device category unit-level indices and OEM content multiples restricted.</div>
            <table class="frost-lock">
                <thead><tr><th>Device Category</th><th>2025 Vol (Mn)</th><th>2035 Vol (Mn)</th><th>Demand Bn</th></tr></thead>
                <tbody>
                    <tr><td>Smartphones</td><td>1,240.00</td><td>1,397.10</td><td>60.77</td></tr>
                    <tr><td>Earwear / TWS</td><td>360.00</td><td>532.89</td><td>7.46</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch5" class="chapter-content max-w-5xl mx-auto">
            <h1>5. Demand Engine: Device-Level Modeling (Automotive & EVs)</h1>
            <p>The automotive sector represents the most critical frontier for value expansion within the passive component industry, driven entirely by the profound architectural shift toward deep electrification and autonomous navigation. The economic landscape here is defined by stringent safety qualifications, harsh operating environments, and zero-defect mandates, which inherently support elevated, highly defensible pricing structures. Component suppliers must prioritize absolute reliability and rigorous lot traceability to penetrate and secure long-term, lucrative positions within modern vehicular supply chains.</p>
            <p>Electric vehicles and advanced driver-assistance systems necessitate a massive, unprecedented increase in the sheer quantity of passive electronic components per chassis. The transition from traditional internal combustion engines to electrified powertrains introduces complex battery management systems, high-voltage traction inverters, and sophisticated in-vehicle infotainment networks, all of which require highly specialized multilayer inductors. These automotive-grade components must exhibit exceptional thermal stability, often rated up to 165°C, and robust resistance to constant mechanical vibration.</p>
            <table>
                <thead><tr><th>Device Category</th><th>2025 Vol (Mn)</th><th>2035 Vol (Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Electric Vehicles (EVs)</td><td>25.00</td><td>61.96</td><td>9.50%</td></tr>
                    <tr><td>ICE / HEV Vehicles</td><td>67.50</td><td>56.29</td><td>-1.80%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch6" class="chapter-content max-w-5xl mx-auto">
            <h1>6. Demand Engine: Device-Level Modeling (IoT Edge Modules)</h1>
            <p>The Internet of Things edge module segment constitutes a rapidly expanding frontier for raw component volume, characterized by the global proliferation of distributed, low-power connectivity nodes. IoT edge modules represent a unique analytical challenge within the demand model, as the astronomical projections for total connected devices must be carefully filtered down to the specific addressable subassemblies that actually utilize multilayer inductors. Module deployment across smart home infrastructure, industrial automation, and logistics tracking applications generates a substantial, persistent volume tailwind.</p>
            <table>
                <thead><tr><th>Category</th><th>2025 Vol (Mn)</th><th>2035 Vol (Mn)</th><th>Demand Bn</th></tr></thead>
                <tbody>
                    <tr><td>IoT Edge Modules</td><td>3,200.00</td><td>6,006.84</td><td>27.03</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch7" class="chapter-content max-w-5xl mx-auto">
            <h1>7. Application & Use-Case Expansion</h1>
            <p>The utility of multilayer inductors is rapidly diversifying far beyond basic signal routing, driven by the increasing complexity of electromagnetic interference mitigation and highly advanced high-frequency communication protocols. A critical driver is the rapid evolution of RF front-end modules designed to support broader 5G spectrums and forthcoming 6G network architectures. Perhaps the most significant emerging use-case is the implementation of Power-over-Coax architectures within high-resolution automotive camera networks. This technology consolidates power delivery and high-speed data transmission onto a single coaxial cable, drastically reducing vehicle wiring harness weight and complexity.</p>
            <div class="insight-highlight">Emerging applications like automotive Power-over-Coax convert traditional signal routing pathways into high-impedance value pools, demanding highly specialized multilayer configurations.</div>
        </article>

        <article id="ch8" class="chapter-content max-w-5xl mx-auto">
            <h1>8. Product Benchmarking & Miniaturization Trends</h1>
            <p>The competitive hierarchy within the multilayer inductor market is fundamentally established by a manufacturer's capacity to execute extreme product miniaturization without degrading core electromagnetic performance. Board space within mobile devices, wearables, and compact automotive modules represents the most expensive and fiercely contested real estate in modern hardware design. The industry's evolutionary trajectory is defined by a relentless transition toward microscopic form factors. Legacy component sizes, such as 0603 and 0402, are systematically being relegated to less space-constrained, lower-margin industrial applications.</p>
            <table>
                <thead><tr><th>Architecture</th><th>Target App</th><th>Capability</th><th>ASP Impact</th></tr></thead>
                <tbody>
                    <tr><td>0201 / 0603</td><td>5G RF & Wearables</td><td>High</td><td>Premium</td></tr>
                    <tr><td>01005 / 0402</td><td>Advanced Mobile RF</td><td>Ultra-High</td><td>High Premium</td></tr>
                    <tr><td>01005 Auto Grade</td><td>Automotive Comm</td><td>Elite</td><td>Maximum</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch9" class="chapter-content max-w-5xl mx-auto">
            <h1>9. Regional Analysis: North America</h1>
            <p>The North American market functions as a critical global nexus for advanced hardware design, complex standard-setting, and high-value component consumption. Despite a limited domestic footprint for electronics assembly, the United States remains a dominant global force in driving component demand through intellectual property creation and system-level architectural design. multilayer inductors consumed within this region typically exhibit a noticeably higher blended average selling price, reflecting a product mix heavily weighted toward rigorous automotive and industrial qualifications.</p>
        </article>

        <article id="ch10" class="chapter-content max-w-5xl mx-auto">
            <h1>10. Regional Analysis: Europe</h1>
            <p>The European market is structurally defined by its unparalleled global concentration of premium automotive engineering and high-end industrial automation. Market demand is overwhelmingly anchored by the continent's accelerated transition toward electrified mobility. This environment mandates the exclusive use of AEC-Q200 qualified multilayer inductors capable of enduring extreme thermal cycling and intense mechanical stress. The European automotive supply chain is notoriously difficult to penetrate, requiring suppliers to demonstrate flawless quality control.</p>
            <table>
                <thead><tr><th>Country / Region</th><th>2025 ($Mn)</th><th>2035 ($Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Germany</td><td>$43.63</td><td>$65.76</td><td>4.19%</td></tr>
                    <tr><td>Total Europe</td><td>$83.63</td><td>$123.76</td><td>4.00%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch11" class="chapter-content max-w-5xl mx-auto">
            <h1>11. Regional Analysis: Asia Pacific (incl. Japan)</h1>
            <p>Asia Pacific operates as the undisputed epicenter of the global industry, serving simultaneously as the primary manufacturing base and the largest consumer market. Japan retains its status as the premier developer of advanced material science, while China dominates absolute volume consumption. emerging regional markets such as India and Vietnam are rapidly establishing themselves as vital alternative manufacturing hubs, driven by global supply chain diversification mandates.</p>
            <table>
                <thead><tr><th>Country / Region</th><th>2025 ($Mn)</th><th>2035 ($Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>China</td><td>$389.78</td><td>$559.88</td><td>3.69%</td></tr>
                    <tr><td>India</td><td>$134.42</td><td>$253.32</td><td>6.54%</td></tr>
                    <tr><td>Japan</td><td>$54.86</td><td>$72.97</td><td>2.89%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch12" class="chapter-content max-w-5xl mx-auto">
            <h1>12. Competitive Landscape: Market Share & Positioning</h1>
            <p>The market operates as a highly concentrated oligopoly. Market share dominance is currently dictated by the ability of a manufacturer to offer a comprehensive, universally qualified product portfolio across all major electronic sectors. The leading entities effectively monopolize the most lucrative segments—such as ultra-miniature radio frequency matching and harsh-environment automotive power—forcing lower-tier competitors into price-wars in consumer segments.</p>
            <table>
                <thead><tr><th>Competitor</th><th>2025 Share (%)</th><th>2035 Share (%)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Murata</td><td>31.00%</td><td>28.00%</td><td>2.82%</td></tr>
                    <tr><td>TDK Corporation</td><td>22.00%</td><td>21.00%</td><td>3.39%</td></tr>
                    <tr><td>Samsung EM</td><td>9.00%</td><td>10.00%</td><td>4.96%</td></tr>
                    <tr><td>Taiyo Yuden</td><td>8.00%</td><td>8.00%</td><td>3.87%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch13" class="chapter-content max-w-5xl mx-auto">
            <h1>13. Competitor Profiling: Murata, Samsung EM & Taiyo Yuden</h1>
            <p>Murata Manufacturing operates as the undisputed benchmark for extreme RF precision, wielding massive architectural influence over smartphone design. Samsung Electro-Mechanics aggressively leverages its massive internal corporate ecosystem to iterate highly reliable compact power components for ADAS. Taiyo Yuden differentiates through an uncompromising focus on fundamental material reliability, deeply embedding its components within the industrial and medical equipment sectors.</p>
        </article>

        <article id="ch14" class="chapter-content max-w-5xl mx-auto">
            <h1>14. Competitor Profiling: Sunlord, YAGEO & Challengers</h1>
            <p>Sunlord Electronics epitomizes the severe threat of rapid domestic localization in China, utilizing intense governmental support to secure massive production volume across new energy sectors. YAGEO (incorporating Chilisin) utilizes immense corporate scale and a highly diversified regional footprint—including massive facilities in Vietnam—to aggressively capture global supply chain diversification trends.</p>
            <div class="teaser-box">🔒 Detailed Net Margin and Yield Analysis per Challenger Restricted.</div>
        </article>

        <article id="ch15" class="chapter-content max-w-5xl mx-auto">
            <h1>15. Value Chain & Profit Pool Analysis</h1>
            <p>Profitability is starkly uneven across the manufacturing sequence. Foundational material integration—dielectric ceramics and high-permeability ferrites—acts as the primary barrier preventing commoditization. The industry profit pool heavily concentrates at the testing and qualification stages, where rigorous certification protocols systematically filter out low-cost commodity manufacturers.</p>
        </article>

        <article id="ch16" class="chapter-content max-w-5xl mx-auto">
            <h1>16. Capacity, Supply-Demand Balance & Footprint</h1>
            <p>Global manufacturing capacity operates under constant tension. Facilities such as TDK's Ouchi factory act as vital innovation anchors. Meanwhile, investments across the ASEAN region, notably in Vietnam and the Philippines, are accelerating as companies seek robust "China+1" supply chains capable of mitigating geopolitical friction.</p>
        </article>

        <article id="ch17" class="chapter-content max-w-5xl mx-auto">
            <h1>17. Trade, Import-Export & Tariff Analysis</h1>
            <p>International trade is increasingly subjected to aggressive geopolitical policy. The imposition of broad ad valorem duties fundamentally alters pricing models. The ability to ship directly from tariff-exempt or favored-nation geographies has emerged as a distinct, highly monetizable competitive advantage.</p>
            <table>
                <thead><tr><th>Country / Region</th><th>Combined Multiplier</th><th>2035 Implication</th></tr></thead>
                <tbody>
                    <tr><td>United States</td><td>1.188</td><td>Max Landed Cost / Tariff Heavy</td></tr>
                    <tr><td>Vietnam</td><td>0.836</td><td>Tariff Bypass / ASEAN Growth</td></tr>
                    <tr><td>China</td><td>0.969</td><td>Scale Optimized / Export Risk</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch18" class="chapter-content max-w-5xl mx-auto">
            <h1>18. Strategic Scenarios: Base, Upside & Downside</h1>
            <p>The base scenario projects steady market expansion driven by 5Gnetwork maturation and automotive electrification. Modeling reveals a $400 million variance between the absolute upside and downside projections for 2035, underscoring that market value is highly elastic and heavily reliant on premium pricing to offset potential consumer device shipment stagnation.</p>
            <table>
                <thead><tr><th>Scenario</th><th>2025 Revenue ($Mn)</th><th>2035 Revenue ($Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Upside (+7% Vol)</td><td>$1,578.91</td><td>$2,308.59</td><td>3.87%</td></tr>
                    <tr><td>Base Case</td><td>$1,446.68</td><td>$2,115.25</td><td>3.87%</td></tr>
                    <tr><td>Downside (-7% Vol)</td><td>$1,305.05</td><td>$1,908.17</td><td>3.87%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch19" class="chapter-content max-w-5xl mx-auto">
            <h1>19. TDK Strategy: Segment Opportunity Mapping</h1>
            <p>TDK corporation operates from a highly advantageous position, capable of dictating market trends. The corporation holds a massive competitive advantage in multi-disciplinary engineering like automotive Power-over-Coax networks. Conversely, the primary strategic risk resides in the mature segments of standard compact ferrite inductors where regional challengers possess structural cost advantages.</p>
            <table>
                <thead><tr><th>Target Segment</th><th>2035 Rev ($Mn)</th><th>Strategic Objective</th><th>Priority</th></tr></thead>
                <tbody>
                    <tr><td>Automotive-Qualified</td><td>$299.60</td><td>Capture Premium EV Modules</td><td>Tier 1</td></tr>
                    <tr><td>RF / High-Frequency</td><td>$1,143.43</td><td>Push Sub-0402 RF Matching</td><td>Tier 1</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>$672.22</td><td>Defend Scale via Automation</td><td>Tier 2</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch20" class="chapter-content max-w-5xl mx-auto">
            <h1>20. Strategic Recommendations & Investment Roadmap</h1>
            <p>The immediate investment priority must be the relentless expansion of automotive-qualified (AEC-Q200) production and accelerated commercialization of sub-0402 architectures. TDK must leverage its global heritage in magnetic materials to co-design integrated inductive solutions directly alongside semiconductor and automotive OEMs.</p>
            <div class="teaser-box">🔒 10-Year Capex allocation and NPV analysis roadmap restricted to purchasers.</div>
            <div class="insight-highlight">TDK's ultimate strategic roadmap dictates a permanent transition from a discrete component supplier to an indispensable architectural partner in next-generation mobility.</div>
        </article>

    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const numChapters = 20;
            const navContainer = document.getElementById('sidebar-nav');
            const chapters = document.querySelectorAll('.chapter-content');
            
            const titles = [
                "1. Executive Summary", "2. Market Core", "3. Pricing Dynamics", "4. Smartphones & Wearables",
                "5. Automotive & EVs", "6. IoT Edge Modules", "7. Use-Case Expansion", "8. Benchmarking & Mini",
                "9. Regional: North America", "10. Regional: Europe", "11. Regional: Asia Pacific", "12. Competitive Control",
                "13. Murata & Samsung Profiles", "14. Regional Challengers", "15. Value Chain & Profits", "16. Capacity & Footprint",
                "17. Trade & Tariffs", "18. Strategic Scenarios", "19. TDK Strategy Matrix", "20. Investment Roadmap"
            ];

            // Build Navigation Menu
            for (let i = 1; i <= numChapters; i++) {
                const navItem = document.createElement('div');
                navItem.className = "nav-item px-8 py-3.5 text-[11px] font-bold uppercase tracking-widest";
                if(i === 1) navItem.classList.add('active');
                navItem.innerText = titles[i-1];
                navItem.dataset.target = 'ch' + i;
                
                navItem.addEventListener('click', () => {
                    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
                    navItem.classList.add('active');
                    chapters.forEach(ch => ch.classList.remove('active'));
                    document.getElementById(navItem.dataset.target).classList.add('active');
                    document.getElementById('main-content').scrollTop = 0;
                });
                navContainer.appendChild(navItem);
            }
        });
    </script>
</body>
</html>
"""

# Dynamic Replacements
final_html = RAW_HTML_CONTENT.replace("__LOGO_PLACEHOLDER__", html_logo)

# Render HTML
components.html(final_html, height=900, scrolling=True)
