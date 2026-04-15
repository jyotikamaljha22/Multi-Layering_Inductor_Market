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

    /* UI ERADICATION */
    [data-testid="stToolbar"] {{ display: none !important; }}
    [data-testid="collapsedControl"] {{ display: none !important; }}
    header[data-testid="stHeader"] {{ background: transparent !important; box-shadow: none !important; }}
    footer {{ display: none !important; }}
    .viewerBadge_container, #viewerBadge_container {{ display: none !important; }}
    
    .block-container {{
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }}

    /* LOGIN GATEWAY STYLING - FIXED INVISIBLE TEXT */
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

    .stButton > button {{
        background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_DARK} 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 15px rgba(74, 12, 37, 0.25) !important;
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
            name = st.text_input("Full Name*")
            email = st.text_input("Corporate Email*")
            password = st.text_input("Access Code*", type="password")
            st.markdown("<br>", unsafe_allow_html=True)
            enter = st.form_submit_button("Enter Boardroom", use_container_width=True)

    if enter:
        if password.strip() == expected_password:
            st.session_state.authenticated = True
            st.session_state.viewer_name = name.strip()
            st.rerun()
        else:
            st.error("❌ Invalid Code.")
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
# HTML DASHBOARD CONTENT
# ----------------------------
html_logo = f'<img src="data:image/svg+xml;base64,{LOGO_B64}" style="height:38px; width:auto; filter: brightness(0) invert(1);" />' if LOGO_B64 else ""

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
        
        /* Smooth Content Transitions */
        .chapter-content { display: none; opacity: 0; transition: opacity 0.4s ease; }
        .chapter-content.active { display: block; opacity: 1; animation: slideUp 0.5s ease-out; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

        /* --- PREMIUM HEADER BLOCK STYLING --- */
        .header-block {
            margin-bottom: 2.5rem;
            padding: 1rem 0;
            border-bottom: 1px solid #e2e8f0;
        }
        .header-kicker {
            color: #C49A23; /* Gold */
            font-size: 0.7rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.2em;
            margin-bottom: 0.75rem;
            display: block;
        }
        .header-main-title {
            font-size: 2.6rem;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.1;
            letter-spacing: -0.03em;
            border-left: 8px solid #4A0C25; /* Deep Burgundy */
            padding-left: 1.5rem;
        }
        
        h2 { font-size: 1.5rem; font-weight: 700; color: #4A0C25; margin-top: 2.5rem; margin-bottom: 1rem; letter-spacing: -0.01em; }

        /* --- DATA TABLES --- */
        table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 2rem 0; background-color: #ffffff; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
        th { background-color: #0f172a; color: #ffffff; font-weight: 700; text-align: left; padding: 1.1rem 1rem; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; }
        td { padding: 1.1rem 1rem; border-bottom: 1px solid #f1f5f9; color: #334155; font-size: 0.9rem; vertical-align: top; line-height: 1.5; }
        tr:hover td { background-color: #fafbfc; }
        
        p { margin-bottom: 1.5rem; line-height: 1.85; color: #475569; text-align: justify; font-size: 1.05rem; }
        
        .frost-lock { filter: blur(8px); opacity: 0.25; pointer-events: none; user-select: none; }
        .teaser-box { background: #fffbeb; border: 1px solid #fde68a; padding: 1.5rem; border-radius: 8px; color: #92400e; font-weight: 700; font-size: 0.9rem; margin-bottom: 2rem; text-align: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }

        .insight-highlight { background: linear-gradient(135deg, #fdfcfd 0%, #fff 100%); border-left: 5px solid #C49A23; padding: 1.75rem; margin: 2.5rem 0; font-style: italic; color: #4A0C25; font-weight: 600; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); font-size: 1.1rem; line-height: 1.6; }
        
        /* SIDEBAR NAV */
        .sidebar { background-color: #020617; } /* Ultra Dark Navy */
        .nav-item { cursor: pointer; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); color: #94a3b8; border-left: 4px solid transparent; }
        .nav-item:hover { background-color: rgba(255,255,255,0.05); color: #ffffff; padding-left: 2.25rem; }
        .nav-item.active { background-color: rgba(255,255,255,0.1); color: #C49A23; font-weight: 800; border-left: 4px solid #C49A23; }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
    </style>
</head>
<body class="flex h-screen overflow-hidden">

    <aside class="w-80 sidebar text-slate-300 flex flex-col h-full overflow-y-auto shrink-0 shadow-2xl z-20">
        <div class="p-8 border-b border-white/10 sticky top-0 sidebar">
            <div class="mb-5">__LOGO_PLACEHOLDER__</div>
            <div class="text-xs font-bold tracking-widest text-[#C49A23] uppercase mb-1">Strategic Market Research</div>
            <h2 class="text-xl font-extrabold text-white leading-tight">Multilayer Inductor <br><span style="color:#94a3b8; font-weight:400;">Global Master Report</span></h2>
        </div>
        <nav class="flex-1 py-4" id="sidebar-nav"></nav>
        <div class="p-6 border-t border-white/10 text-[10px] text-slate-500 uppercase tracking-widest bg-black/20">
            &copy; 2026 SMR Group • Confidential
        </div>
    </aside>

    <main class="flex-1 overflow-y-auto bg-[#FBFBFC] relative p-8 md:p-12 lg:p-24 scroll-smooth" id="main-content">
        
        <article id="ch1" class="chapter-content active max-w-5xl mx-auto">
            <div class="header-block">
                <span class="header-kicker">Executive Strategic Pillar 01</span>
                <h1 class="header-main-title">Executive Summary & Strategic Objective</h1>
            </div>
            <p>The global multilayer inductor market operates as a foundational pillar within modern electronic architecture, driven by the absolute necessity for precision radio frequency matching and robust power regulation. Demand is structurally tied to the proliferation of compact, high-density electronic assemblies across advanced mobile, industrial, and automotive platforms. The underlying economic landscape heavily rewards extreme miniaturization and stringent environmental qualification over pure production scale.</p>
            <p>The trajectory of the multilayer inductor sector is fundamentally defined by the transition from volumetric consumer electronics growth toward value-dense automotive and industrial applications. Historically, market expansion relied on the sheer unit scale of smartphone and generic computing device production, which offered reliable but low-margin revenue streams. Contemporary market dynamics, however, indicate that raw unit volumes no longer correlate linearly with revenue generation, as advanced applications require highly specialized, premium-priced components. Consequently, manufacturers that successfully pivot their portfolios toward stringent qualification standards secure disproportionate shares of the expanding industry profit pool.</p>
            
            <table>
                <thead><tr><th>Segment</th><th>2025 ($Mn)</th><th>2035 ($Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td class="font-bold">RF / High-Frequency</td><td>$839.12</td><td>$1,143.43</td><td>3.14%</td></tr>
                    <tr><td class="font-bold text-[#C49A23]">Automotive-Qualified</td><td>$132.75</td><td>$299.60</td><td class="font-bold text-emerald-600">8.48%</td></tr>
                    <tr><td class="font-bold">Compact Ferrite / NFC</td><td>$474.81</td><td>$672.22</td><td>3.54%</td></tr>
                </tbody>
            </table>
            <div class="insight-highlight">Strategic Objective: TDK must aggressively pivot manufacturing capabilities toward the Automotive sector, which represents the primary engine for future value creation across the entire passive component ecosystem.</div>
        </article>

        <article id="ch2" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block">
                <span class="header-kicker">Strategic Core Analysis 02</span>
                <h1 class="header-main-title">Market Core: Global Size, Volume, and Trajectory</h1>
            </div>
            <p>The global multilayer inductor market represents a highly concentrated economic ecosystem where total value is governed by the intersection of aggregate device shipments and individual component complexity. Demand is perpetually driven by the necessity to route complex signals through increasingly dense, miniaturized printed circuit boards within mobility and edge-computing hardware. Sustained revenue expansion therefore requires continuous technological iteration to satisfy the severe spatial limitations and thermal constraints of contemporary hardware architectures.</p>
            <p>The absolute scale is anchored by an immense volume of individual component shipments, which are projected to expand significantly over the forecast horizon. This volume expansion is driven by the increasing electronic content per device across virtually all major hardware categories, successfully counterbalancing the plateauing shipment growth of mature consumer devices like smartphones. The manufacturing base faces immense pressure to scale physical output while strictly maintaining the precise electromagnetic characteristics required by telecommunications and automotive end-users, leaving no margin for quality degradation.</p>
            
            <table>
                <thead><tr><th>Segment</th><th>2025 (Bn units)</th><th>2035 (Bn units)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>RF / High-Frequency</td><td>38.14</td><td>54.45</td><td>3.62%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>35.17</td><td>53.78</td><td>4.33%</td></tr>
                    <tr><td class="font-bold text-[#C49A23]">Automotive-Qualified</td><td>3.69</td><td>7.88</td><td class="font-bold text-emerald-600">7.88%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch3" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block">
                <span class="header-kicker">Value Metrics Pillar 03</span>
                <h1 class="header-main-title">Pricing & Value Dynamics</h1>
            </div>
            <p>Segment economics within the multilayer inductor industry are strictly dictated by the average selling price, which remains highly sensitive to the specific material composition, precision, and operational rating of the manufactured component. The financial viability of manufacturing operations relies heavily on actively protecting these price points against the natural deflationary pressures inherent in mature electronic component supply chains. Maintaining robust operating margins requires relentless innovation in proprietary sintering and layering techniques to continually justify premium pricing architectures to procurement teams.</p>
            <div class="insight-highlight">Premium component pricing is sustained strictly by thermal reliability thresholds and structural qualification parameters, creating a formidable economic moat against high-volume consumer commoditization.</div>
            <table>
                <thead><tr><th>Segment</th><th>2025 ($/unit)</th><th>2035 ($/unit)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td class="font-bold text-[#C49A23]">Automotive-Qualified</td><td>0.0360</td><td>0.0380</td><td class="text-emerald-600 font-bold">0.54%</td></tr>
                    <tr><td>RF / High-Frequency</td><td>0.0220</td><td>0.0210</td><td>-0.46%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>0.0135</td><td>0.0125</td><td>-0.76%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch4" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block">
                <span class="header-kicker">Device Modeling 04</span>
                <h1 class="header-main-title">Device Modeling: Smartphones & Wearables</h1>
            </div>
            <p>The smartphone ecosystem remains the largest single consumer of multilayer inductors. The transition to higher frequency bands necessitates a corresponding increase in the sheer quantity of precision inductors required to prevent signal degradation and EMI.</p>
            <div class="teaser-box">🔒 High-Resolution OEM attach rates and content-per-handset indices are restricted to purchasers.</div>
            <table class="frost-lock">
                <thead><tr><th>OEM</th><th>2025 Content</th><th>2035 Content</th><th>CAGR</th></tr></thead>
                <tbody><tr><td>Apple / Samsung</td><td>40-45 units</td><td>[LOCKED]</td><td>$$$</td></tr></tbody>
            </table>
        </article>

        <article id="ch5" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">Device Modeling 05</span><h1 class="header-main-title">Device Modeling: Automotive & EVs</h1></div>
            <p>Electric vehicles introducing complex battery management systems and high-voltage traction inverters, all of which require specialized inductors. These AEC-Q200 grade components must exhibit exceptional thermal stability, often rated up to 165°C.</p>
             <table>
                <thead><tr><th>Device Category</th><th>2025 Vol (Mn)</th><th>2035 Vol (Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Electric Vehicles (EVs)</td><td>25.00</td><td>61.96</td><td>9.50%</td></tr>
                    <tr><td>ICE / HEV Vehicles</td><td>67.50</td><td>56.29</td><td>-1.80%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch19" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block">
                <span class="header-kicker">Strategic Positioning 19</span>
                <h1 class="header-main-title">TDK Strategy: Win/Loss Matrix</h1>
            </div>
            <p>TDK holds a massive competitive advantage ("Win") in arenas requiring multi-disciplinary engineering, such as automotive Power-over-Coax networks and high-temperature in-vehicle networking. TDK must utilize its elite Japanese manufacturing nodes purely as specialized capability anchors.</p>
            <table>
                <thead><tr><th>Competitive Vector</th><th>Outcome</th><th>Strategic Goal</th></tr></thead>
                <tbody>
                    <tr><td>Auto PoC Networks</td><td class="font-bold text-emerald-600">Clear Win Zone</td><td>Monopolize Reference Designs</td></tr>
                    <tr><td>01005 Miniaturization</td><td class="font-bold text-yellow-600">Contested</td><td>Maintain Parity with Murata</td></tr>
                    <tr><td>Domestic China Consumer</td><td class="font-bold text-rose-600">Loss Zone</td><td>Managed Defensive Retreat</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch20" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block">
                <span class="header-kicker">Future Roadmap 20</span>
                <h1 class="header-main-title">Recommendations & Investment Roadmap</h1>
            </div>
            <p>Immediate investment priority must be the relentless expansion of automotive-qualified production and acceleration of sub-0402 architectures. TDK must transition from a discrete component vendor to an indispensable architectural partner.</p>
            <div class="teaser-box">🔒 Chapter 20: Full NPV analysis of Ouchi Factory Retooling is Restricted.</div>
        </article>

        </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const numChapters = 20;
            const navContainer = document.getElementById('sidebar-nav');
            const chapters = document.querySelectorAll('.chapter-content');
            
            const titles = [
                "Executive Summary", "Global Size & Volume", "Pricing Dynamics", "Smartphones & Wearables",
                "Automotive & EVs", "IoT Edge Modules", "Use-Case Expansion", "Miniaturization Trends",
                "Regional: N. America", "Regional: Europe", "Regional: APAC", "Market Share Control",
                "Murata & Samsung Profiles", "Challenger Profiles", "Value Chain & Profits", "Capacity & Footprint",
                "Trade & Tariffs", "Strategic Scenarios", "TDK Win/Loss Matrix", "Investment Roadmap"
            ];

            for (let i = 1; i <= numChapters; i++) {
                const navItem = document.createElement('div');
                navItem.className = "nav-item px-8 py-3.5 text-[11px] font-bold uppercase tracking-widest";
                if(i === 1) navItem.classList.add('active');
                navItem.innerText = i + ". " + titles[i-1];
                navItem.dataset.target = 'ch' + i;
                
                navItem.addEventListener('click', () => {
                    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
                    navItem.classList.add('active');
                    chapters.forEach(ch => ch.classList.remove('active'));
                    const target = document.getElementById(navItem.dataset.target);
                    if(target) target.classList.add('active');
                    document.getElementById('main-content').scrollTop = 0;
                });
                navContainer.appendChild(navItem);
            }
        });
    </script>
</body>
</html>
"""

# Replace the placeholder with the dynamic logo
final_html = RAW_HTML_CONTENT.replace("__LOGO_PLACEHOLDER__", html_logo)

# Render HTML inside Streamlit container
components.html(final_html, height=880, scrolling=True)
