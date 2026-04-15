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
            
        st.markdown(f"<p style='text-align:center; color:{GOLD}; font-weight:800; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:30px; font-size: 0.9rem;'>TDK Corporation Advisory Portal</p>", unsafe_allow_html=True)
        
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
# HTML DASHBOARD CONTENT
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
        
        /* Premium Table Styling */
        table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 1.5rem 0; background-color: #ffffff; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; }
        th { background-color: #4A0C25; color: #ffffff; font-weight: 700; text-align: left; padding: 1rem; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }
        td { padding: 1rem; border-bottom: 1px solid #f1f5f9; color: #334155; font-size: 0.875rem; vertical-align: top; }
        tr:hover td { background-color: #fafafa; }
        
        /* Paragraph formatting */
        p { margin-bottom: 1.5rem; line-height: 1.8; color: #475569; text-align: justify; font-size: 1rem; }
        h1 { font-size: 2.2rem; font-weight: 800; color: #1e293b; margin-bottom: 1.5rem; border-bottom: 4px solid #C49A23; padding-bottom: 0.5rem; letter-spacing: -0.02em; }
        h2 { font-size: 1.5rem; font-weight: 700; color: #4A0C25; margin-top: 2rem; margin-bottom: 1rem; }
        
        /* Teaser Mask / Blur */
        .frost-lock { filter: blur(8px); opacity: 0.2; pointer-events: none; user-select: none; }
        .teaser-box { background: #fffbeb; border: 1px solid #fde68a; padding: 1.5rem; border-radius: 8px; color: #92400e; font-weight: 600; font-size: 0.9rem; margin-bottom: 1.5rem; text-align: center; }

        /* Insight Box */
        .insight-highlight { background: linear-gradient(135deg, #fdfcfd 0%, #fff 100%); border-left: 5px solid #C49A23; padding: 1.5rem; margin: 2rem 0; font-style: italic; color: #4A0C25; font-weight: 600; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
        
        /* Sidebar Navigation */
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
            <h2 class="text-xl font-extrabold text-white leading-tight">Multilayer Inductor <br>Global Master Report</h2>
            <div class="text-xs text-slate-400 mt-2 font-medium">Internal Advisory Document</div>
        </div>
        <nav class="flex-1 py-4" id="sidebar-nav"></nav>
        <div class="p-6 border-t border-white/10 text-[10px] text-slate-500 uppercase tracking-widest bg-black/20">
            &copy; 2026 SMR Group • Confidential
        </div>
    </aside>

    <main class="flex-1 overflow-y-auto bg-slate-50 relative p-8 md:p-12 lg:p-20 scroll-smooth" id="main-content">
        
        <article id="ch1" class="chapter-content active max-w-5xl mx-auto">
            <h1>1. Executive Summary & Strategic Objective</h1>
            <p>The global multilayer inductor market is at a definitive crossroads. As consumer device volumes plateau, value creation is migrating toward high-reliability automotive and precision RF matching sub-systems. Manufacturers possessing integrated ceramic material science capabilities stand to capture the majority of the projected $2.1B profit pool by 2035.</p>
            <table>
                <thead><tr><th>Metric</th><th>2025</th><th>2035</th><th>CAGR</th></tr></thead>
                <tbody>
                    <tr><td>Market Revenue ($Mn)</td><td>$1,446.68</td><td>$2,115.25</td><td>3.87%</td></tr>
                    <tr><td>Unit Volume (Bn)</td><td>77.0 Bn</td><td>116.1 Bn</td><td>4.19%</td></tr>
                    <tr><td>Auto-Grade Share (%)</td><td>9.18%</td><td>14.16%</td><td>8.48%</td></tr>
                </tbody>
            </table>
            <div class="insight-highlight">Key Strategic Priority: Transition from commoditized smartphone volume toward ultra-high-frequency (UHF) RF and AEC-Q200 Grade 0 components to insulate margins from 3.5% annual consumer price erosion.</div>
        </article>

        <article id="ch2" class="chapter-content max-w-5xl mx-auto">
            <h1>2. Global Size, Volume & Trajectory</h1>
            <p>Physical volume demand is projected to expand to 116.11 Bn units by 2035. However, a structural decoupling is occurring: unit demand (+4.2%) is outpacing revenue (+3.87%), signaling a relentless deflationary pressure in legacy form factors.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 (Bn)</th><th>2035 (Bn)</th><th>CAGR</th></tr></thead>
                <tbody>
                    <tr><td>RF / High-Frequency</td><td>38.14</td><td>54.45</td><td>3.62%</td></tr>
                    <tr><td>Compact Ferrite</td><td>35.17</td><td>53.78</td><td>4.33%</td></tr>
                    <tr><td>Automotive-Qualified</td><td>3.69</td><td>7.88</td><td>7.88%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch3" class="chapter-content max-w-5xl mx-auto">
            <h1>3. Pricing & Value Dynamics</h1>
            <p>Pricing remains highly sensitive to material science thresholds. Automotive-grade inductors are the only category demonstrating positive price appreciation, providing a "Value Lifeboat" for Japanese incumbents against aggressive regional price wars.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 ASP ($)</th><th>2035 ASP ($)</th><th>CAGR</th></tr></thead>
                <tbody>
                    <tr><td>Automotive-Grade</td><td>$0.0360</td><td>$0.0380</td><td>0.54%</td></tr>
                    <tr><td>Consumer RF</td><td>$0.0220</td><td>$0.0210</td><td>-0.46%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch4" class="chapter-content max-w-5xl mx-auto">
            <h1>4. Device Modeling: Smartphones & Wearables</h1>
            <p>The smartphone content-per-device continues to expand as 5G architectures demand denser antenna matching. However, the volume anchor is shifting toward True Wireless Stereo (TWS) and Health-wearables requiring sub-0201 architectures.</p>
            <div class="teaser-box">🔒 15-Device category unit-level indices are reserved for purchasers.</div>
            <table class="frost-lock">
                <thead><tr><th>Device</th><th>2025 Content</th><th>2035 Content</th><th>Value Pool</th></tr></thead>
                <tbody>
                    <tr><td>Smartphone</td><td>40-45 units</td><td>[HIDDEN]</td><td>$$$</td></tr>
                    <tr><td>Hearables</td><td>12-18 units</td><td>[HIDDEN]</td><td>$$$</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch5" class="chapter-content max-w-5xl mx-auto">
            <h1>5. Device Modeling: Automotive & EVs</h1>
            <p>Electric Vehicles represent the ultimate "Component Density Sink." An EV chassis requires nearly 3x the inductor volume of a legacy ICE vehicle, focusing on battery management systems (BMS) and traction inverters.</p>
            <table>
                <thead><tr><th>Vehicle Type</th><th>2025 Bn units</th><th>2035 Bn units</th><th>CAGR</th></tr></thead>
                <tbody>
                    <tr><td>Electric Vehicles (EV)</td><td>3.50</td><td>10.53</td><td>11.6%</td></tr>
                    <tr><td>ICE / HEV</td><td>3.71</td><td>3.60</td><td>-0.30%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch6" class="chapter-content max-w-5xl mx-auto">
            <h1>6. Device Modeling: IoT Edge Modules</h1>
            <p>IoT modules generate a massive, undeniable volume tailwind (27.0 Bn units by 2035). However, the segment remains overwhelmingly volume-dependent, prioritizing raw scale over individual premium pricing.</p>
        </article>

        <article id="ch7" class="chapter-content max-w-5xl mx-auto">
            <h1>7. Application & Use-Case Expansion</h1>
            <p>Emerging applications like <strong>Power-over-Coax (PoC)</strong> and <strong>NFC Coupling</strong> are converting traditional signal routing pathways into high-impedance value pools, demanding highly specialized multilayer configurations.</p>
        </article>

        <article id="ch8" class="chapter-content max-w-5xl mx-auto">
            <h1>8. Product Benchmarking & Miniaturization</h1>
            <p>01005 (imperial) architectures represent the absolute pinnacle of current electrical engineering. Mastering yield stability at this scale serves as a nearly impenetrable tech moat against 80% of regional competitors.</p>
            <table>
                <thead><tr><th>Size (Imperial)</th><th>Tech Barrier</th><th>Yield Sensitivity</th><th>Moat Level</th></tr></thead>
                <tbody>
                    <tr><td>0402</td><td>Standard</td><td>Low</td><td>Low</td></tr>
                    <tr><td>0201</td><td>High</td><td>Medium</td><td>High</td></tr>
                    <tr><td>01005</td><td>Elite</td><td>Extreme</td><td>Maximum</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch9" class="chapter-content max-w-5xl mx-auto"><h1>9. Regional Analysis: North America</h1><p>US remains the premier nexus for hardware design Wins. Strategic focus must stay on Silicon Valley reference designs to lock-in downstream Asian production.</p></article>
        <article id="ch10" class="chapter-content max-w-5xl mx-auto"><h1>10. Regional Analysis: Europe</h1><p>Germany commands the high-margin automotive sector. Tier-1 partnerships here are mandatory for 10-year revenue visibility.</p></article>
        <article id="ch11" class="chapter-content max-w-5xl mx-auto">
            <h1>11. Regional Analysis: Asia Pacific</h1>
            <p>India is the breakout growth frontier (+7.3% CAGR), while China remains the volume anchor. Footprint diversification (Vietnam) is now a mandatory risk mitigation strategy.</p>
            <div class="teaser-box">🔒 45-Country corridor unit flow analysis locked.</div>
        </article>

        <article id="ch12" class="chapter-content max-w-5xl mx-auto">
            <h1>12. Competitive Landscape: Market Share</h1>
            <p>The market is a concentrated oligopoly. The top 5 players command 87% share. Japanese engineering remains the dominant gravitational force.</p>
            <table>
                <thead><tr><th>Tier</th><th>Share (%)</th><th>Primary Moat</th></tr></thead>
                <tbody>
                    <tr><td>Elite (TDK/Murata)</td><td>53.0%</td><td>Material Science / 01005</td></tr>
                    <tr><td>Challengers (Sunlord/YAGEO)</td><td>13.0%</td><td>Local Scale / Price Attrition</td></tr>
                </tbody>
            </table>
        </article>
        <article id="ch13" class="chapter-content max-w-5xl mx-auto"><h1>13. Competitor Profiling: Murata & Samsung</h1><p>Murata's LQP02HQ_Z2 series exemplifies the transfer of mobile tech into Auto-RF. Samsung E-M leverages internal MLCC synergies to undercut power inductor competitors.</p></article>
        <article id="ch14" class="chapter-content max-w-5xl mx-auto"><h1>14. Competitor Profiling: Regional Challengers</h1><p>Sunlord and YAGEO are yield-locking 0201 formats, threatening legacy Japanese margins in high-volume smartphone lines.</p></article>

        <article id="ch15" class="chapter-content max-w-5xl mx-auto">
            <h1>15. Value Chain & Profit Pool</h1>
            <p>Profit pools are unevenly distributed. Testing and Automotive Qualification protocols generate 2.5x the EBITDA per unit compared to pure physical layering.</p>
        </article>
        <article id="ch16" class="chapter-content max-w-5xl mx-auto"><h1>16. Capacity & Supply Balance</h1><p>A "China+1" strategy is now the industry standard to bypass geopolitical supply shocks. Vietnam expansion is the primary capacity vector for 2030.</p></article>
        <article id="ch17" class="chapter-content max-w-5xl mx-auto">
            <h1>17. Trade & Tariff Analysis</h1>
            <p>US IEEPA and Section 122 duties create massive landed-cost distortions. Vietnam (ASEAN) provides a critical 0.83x multiplier advantage for tariff bypass.</p>
        </article>

        <article id="ch18" class="chapter-content max-w-5xl mx-auto">
            <h1>18. Strategic Scenarios</h1>
            <p>Upside Case ($2.31Bn) depends on hyper-adoption of redundant ADAS sensors. Downside ($1.91Bn) assumes prolonged consumer stagnation and 6G launch delays.</p>
        </article>
        <article id="ch19" class="chapter-content max-w-5xl mx-auto">
            <h1>19. TDK Strategy: Win/Loss Matrix</h1>
            <p>TDK wins by monopolizing Reference Designs in Automotive PoC and sub-0402 RF Matching. TDK "Loses" (retreats) in standard NFC filtering to protect overall group margins.</p>
        </article>
        <article id="ch20" class="chapter-content max-w-5xl mx-auto">
            <h1>20. Recommendations & Roadmap</h1>
            <p>Capital must be aggressively diverted away from legacy formats toward high-temperature materials. The Ouchi and Akita mother-factories must become innovation-only anchors.</p>
            <div class="teaser-box">🔒 10-Year Capex & ROI roadmap (NPV Analysis) restricted to full report.</div>
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
                "Regional: N. America", "Regional: Europe", "Regional: APAC", "Competitive Landscape",
                "Murata & Samsung Profiles", "Challenger Profiles", "Value Chain & Profits", "Capacity Balance",
                "Trade & Tariffs", "Strategic Scenarios", "TDK Win/Loss Matrix", "Investment Roadmap"
            ];

            for (let i = 1; i <= numChapters; i++) {
                const navItem = document.createElement('div');
                navItem.className = "nav-item px-8 py-2.5 text-[11px] font-bold uppercase tracking-widest";
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

# Render
final_html = RAW_HTML_CONTENT.replace("__LOGO_PLACEHOLDER__", html_logo)
components.html(final_html, height=850, scrolling=True)
