import os
import csv
import base64
from datetime import datetime, timezone
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Strategic Market Research | TDK Corporation Boardroom",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded", 
)

# ----------------------------
# THEME COLORS & LOGO LOGIC
# ----------------------------
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

# ----------------------------
# CSS HIDING & MAIN UI POLISH
# ----------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}

    /* --- PERMANENT UI ERADICATION --- */
    [data-testid="stSidebar"] {{ display: none !important; }}
    [data-testid="collapsedControl"] {{ display: none !important; }}
    [data-testid="stToolbar"] {{ display: none !important; }}
    header[data-testid="stHeader"] {{ display: none !important; }}
    footer {{ display: none !important; }}
    .viewerBadge_container, #viewerBadge_container {{ display: none !important; }}
    
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }}

    /* --- LOGIN FORM STYLING --- */
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

    st.markdown("<div style='margin-top: 12vh;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        if LOGO_B64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:65px; margin-bottom:20px;" /></div>', unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='text-align:center; color:{BURGUNDY}; font-weight:800; font-size:2.2rem; margin-bottom:0;'>Strategic Market Research</h1>", unsafe_allow_html=True)
            
        st.markdown(f"<p style='text-align:center; color:{GOLD}; font-weight:800; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:30px; font-size: 0.9rem;'>TDK Corporation Executive Advisory</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            st.markdown(f"<h3 style='color:#1e293b; font-weight:800; margin-bottom:20px; text-align:center; font-size: 1.4rem;'>🔐 Secure Authentication</h3>", unsafe_allow_html=True)
            name = st.text_input("Full Name*")
            email = st.text_input("Email*")
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
# HTML DASHBOARD CONTENT (20 CHAPTERS)
# ----------------------------
html_logo = f'<img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:32px; width:auto; filter: brightness(0) invert(1);" />' if LOGO_B64 else ""

RAW_HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Multilayer Inductor Market (2025–2035)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #f8fafc; margin: 0; }
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
            <h2 class="text-xl font-extrabold text-white leading-tight">Multilayer Inductor <br>Global Report</h2>
        </div>
        <nav class="flex-1 py-4" id="sidebar-nav"></nav>
        <div class="p-6 border-t border-white/10 text-[10px] text-slate-500 uppercase tracking-widest bg-black/20">
            &copy; 2026 SMR Group • Confidential
        </div>
    </aside>

    <main class="flex-1 overflow-y-auto bg-slate-50 relative p-8 md:p-12 lg:p-20 scroll-smooth" id="main-content">
        
        <article id="ch1" class="chapter-content active max-w-5xl mx-auto">
            <h1>1. Executive Summary & Strategic Objective</h1>
            <p>The global multilayer inductor market operates as a foundational pillar within modern electronic architecture, driven by the absolute necessity for precision radio frequency matching and robust power regulation. Strategic objectives demand a precise alignment of manufacturing capabilities with high-growth end markets to mitigate the risks of commoditization.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 ($Mn)</th><th>2035 ($Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>RF / High-Frequency</td><td>$839.12</td><td>$1,143.43</td><td>3.14%</td></tr>
                    <tr><td>Automotive-Qualified</td><td>$132.75</td><td>$299.60</td><td>8.48%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>$474.81</td><td>$672.22</td><td>3.54%</td></tr>
                </tbody>
            </table>
            <div class="insight-highlight">Value creation in the multilayer inductor market is rapidly decoupling from pure unit volumes, heavily favoring automotive qualification and ultra-high-frequency capabilities as the ultimate drivers of corporate profitability.</div>
        </article>

        <article id="ch2" class="chapter-content max-w-5xl mx-auto">
            <h1>2. Market Core: Global Size, Volume & Trajectory</h1>
            <p>Demand is perpetually driven by the necessity to route complex signals through increasingly dense, miniaturized PCBs. The absolute scale is anchored by an immense volume of individual shipments, projected to reach 116 Bn units by 2035.</p>
            <div class="teaser-box">🔒 Granular Unit-Level Forecast (Bn units) Restricted.</div>
            <table class="frost-lock">
                <thead><tr><th>Segment</th><th>2025 (Bn units)</th><th>2030 (Bn units)</th><th>2035 (Bn units)</th></tr></thead>
                <tbody>
                    <tr><td>Total Volume Demand</td><td>77.00</td><td>93.60</td><td>116.11</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch3" class="chapter-content max-w-5xl mx-auto">
            <h1>3. Pricing & Value Dynamics</h1>
            <p>Segment economics are strictly dictated by the ASP, which remains highly sensitive to material composition. Automotive-qualified inductors command the highest premium due to exhaustive testing protocols and AEC-Q200 standards.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 ASP ($)</th><th>2035 ASP ($)</th><th>Price Trend</th></tr></thead>
                <tbody>
                    <tr><td>Automotive-Qualified</td><td>$0.0360</td><td>$0.0380</td><td>Appreciating</td></tr>
                    <tr><td>RF / High-Frequency</td><td>$0.0220</td><td>$0.0210</td><td>Deflationary</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch4" class="chapter-content max-w-5xl mx-auto">
            <h1>4. Demand Engine: Device-Level Modeling (Mobile)</h1>
            <p>Smartphones and wearable devices constitute the absolute baseline of global consumption. The vital metric is the content-per-device multiple, expanding as OEMs integrate complex 5G RF front-ends.</p>
            <table>
                <thead><tr><th>Device Category</th><th>2025 Vol (Mn)</th><th>2035 Vol (Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Smartphones</td><td>1,240.00</td><td>1,397.10</td><td>1.20%</td></tr>
                    <tr><td>Earwear / TWS</td><td>360.00</td><td>532.89</td><td>4.00%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch5" class="chapter-content max-w-5xl mx-auto">
            <h1>5. Demand Engine: Device-Level Modeling (Automotive)</h1>
            <p>The automotive sector represents the most critical frontier for value expansion. Electric vehicles introduce complex battery management and high-voltage inverters requiring specialized inductors rated up to 165°C.</p>
            <table>
                <thead><tr><th>Device Category</th><th>2025 Demand (Bn)</th><th>2035 Demand (Bn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Electric Vehicles (EVs)</td><td>3.50</td><td>10.53</td><td>9.50%</td></tr>
                    <tr><td>ICE / HEV Vehicles</td><td>3.71</td><td>3.60</td><td>-1.80%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch6" class="chapter-content max-w-5xl mx-auto">
            <h1>6. Demand Engine: Device-Level Modeling (IoT)</h1>
            <p>IoT edge modules constitute a rapidly expanding frontier for raw volume. Success demands hyper-efficient manufacturing operations capable of delivering massive quantities of standardized parts without margin collapse.</p>
        </article>

        <article id="ch7" class="chapter-content max-w-5xl mx-auto">
            <h1>7. Application & Use-Case Expansion</h1>
            <p>The utility is diversifying beyond basic routing into Power-over-Coax (PoC) architectures for automotive cameras, and NFC coupling for mobile payments.</p>
        </article>

        <article id="ch8" class="chapter-content max-w-5xl mx-auto">
            <h1>8. Product Benchmarking & Miniaturization</h1>
            <p>The hierarchy is established by the capacity to execute extreme miniaturization. The vanguard is perfected in mass production of 0201 and 01005 architectures.</p>
            <table>
                <thead><tr><th>Architecture</th><th>Target App</th><th>Tech Capability</th><th>Qual</th></tr></thead>
                <tbody>
                    <tr><td>0201 / 0603</td><td>5G RF</td><td>High</td><td>Comm</td></tr>
                    <tr><td>01005 / 0402</td><td>Advanced Mobile</td><td>Ultra-High</td><td>Premium</td></tr>
                    <tr><td>01005 Auto Grade</td><td>Auto Comm</td><td>Elite</td><td>AEC-Q200</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch9" class="chapter-content max-w-5xl mx-auto"><h1>9. Regional Analysis: North America</h1><p>The US market functions as a critical nexus for hardware design and high-value component consumption, prioritizing ADAS and enterprise server infrastructure.</p></article>
        <article id="ch10" class="chapter-content max-w-5xl mx-auto"><h1>10. Regional Analysis: Europe</h1><p>Europe is structurally defined by premium automotive engineering. Regional demand is anchored in Germany, requiring AEC-Q200 qualified inductors for thermal cycling.</p></article>
        <article id="ch11" class="chapter-content max-w-5xl mx-auto"><h1>11. Regional Analysis: Asia Pacific</h1><p>Asia Pacific operates as the irreplaceable manufacturing base. While Japan retains process dominance, India emerges as the high-growth frontier with a 6.54% CAGR.</p></article>

        <article id="ch12" class="chapter-content max-w-5xl mx-auto">
            <h1>12. Competitive Landscape: Market Share</h1>
            <p>The market is a concentrated oligopoly. Murata and TDK collectively secure over 50% of the market, leaning on legacy Japanese passive component engineering.</p>
            <div class="teaser-box">🔒 Granular Market Share Projections Restricted.</div>
            <table class="frost-lock">
                <thead><tr><th>Competitor</th><th>2025 Share (%)</th><th>2035 Share (%)</th></tr></thead>
                <tbody>
                    <tr><td>Murata</td><td>31.00%</td><td>[LOCKED]</td></tr>
                    <tr><td>TDK</td><td>22.00%</td><td>[LOCKED]</td></tr>
                </tbody>
            </table>
        </article>
        <article id="ch13" class="chapter-content max-w-5xl mx-auto"><h1>13. Competitor Profiling: Murata & Samsung</h1><p>Murata's strategy transfers mobile tech into the automotive sector. Samsung leverages cross-divisional synergies to iterate reliable 165°C compact power components.</p></article>
        <article id="ch14" class="chapter-content max-w-5xl mx-auto"><h1>14. Competitor Profiling: Regional Challengers</h1><p>Sunlord and YAGEO utilize local scale and governmental support within China to systematically move up the value chain from commodity to competitive RF inductors.</p></article>

        <article id="ch15" class="chapter-content max-w-5xl mx-auto"><h1>15. Value Chain & Profit Pool Analysis</h1><p>Profit pools are uneven. Material formulation and certification generate the vast majority of profit, while generic manufacturing stages face rapid commoditization.</p></article>
        <article id="ch16" class="chapter-content max-w-5xl mx-auto"><h1>16. Capacity & Supply-Demand Balance</h1><p>The industry standard is now "China+1." Footprint diversification in Vietnam and Philippines is mandatory to mitigate geopolitical shocks.</p></article>
        <article id="ch17" class="chapter-content max-w-5xl mx-auto">
            <h1>17. Trade & Tariff Analysis</h1>
            <p>Landed costs are distorted by US Section 122 duties. Tariff-exempt geographies (ASEAN) emerge as a highly monetizable competitive advantage.</p>
            <table>
                <thead><tr><th>Geography</th><th>Regional Multiplier</th><th>Combined Multiplier</th></tr></thead>
                <tbody>
                    <tr><td>United States</td><td>1.08</td><td>1.188</td></tr>
                    <tr><td>Vietnam</td><td>0.95</td><td>0.836</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch18" class="chapter-content max-w-5xl mx-auto"><h1>18. Strategic Scenarios (Base, Upside, Downside)</h1><p>Modeling reveals a $400M variance between upside ($2.31Bn) and downside ($1.91Bn) for 2035, driven by the velocity of EV penetration.</p></article>
        <article id="ch19" class="chapter-content max-w-5xl mx-auto">
            <h1>19. TDK Strategy: Win/Loss Matrix</h1>
            <p>TDK holds an elite advantage in Automotive PoC Networks. The strategic loss zone is identified as domestic China scale for standard compact ferrite filters.</p>
        </article>
        <article id="ch20" class="chapter-content max-w-5xl mx-auto">
            <h1>20. Strategic Recommendations & Roadmap</h1>
            <p>Relentless expansion of AEC-Q200 production and acceleration of sub-0402 architectures are non-negotiable for terminal margin defense.</p>
            <div class="teaser-box">🔒 Full Capex & ROI Investment Roadmap Restricted to Purchases.</div>
        </article>

    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const numChapters = 20;
            const navContainer = document.getElementById('sidebar-nav');
            const chapters = document.querySelectorAll('.chapter-content');
            
            const titles = [
                "Executive Summary", "Size & Trajectory", "Pricing Dynamics", "Smartphones & Wearables",
                "Automotive & EVs", "IoT Edge Modules", "Use-Case Expansion", "Benchmarking & Mini",
                "N. America Analysis", "Europe Analysis", "Asia Pacific Analysis", "Market Share Control",
                "Murata & Samsung Profiles", "Regional Challengers", "Value Chain & Profits", "Capacity & Footprint",
                "Trade & Tariffs", "Strategic Scenarios", "TDK Win/Loss Matrix", "Investment Roadmap"
            ];

            for (let i = 1; i <= numChapters; i++) {
                const navItem = document.createElement('div');
                navItem.className = "nav-item px-8 py-3 text-[11px] font-bold uppercase tracking-widest";
                if(i === 1) navItem.classList.add('active');
                navItem.innerText = i + ". " + titles[i-1];
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

# Render HTML inside Streamlit container
# Using simple replace for logo to keep code clean and safe
final_html = RAW_HTML_CONTENT.replace("__LOGO_PLACEHOLDER__", html_logo)
components.html(final_html, height=850, scrolling=True)
