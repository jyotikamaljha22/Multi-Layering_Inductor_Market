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
        .chapter-content { display: none; opacity: 0; transition: opacity 0.4s ease; }
        .chapter-content.active { display: block; opacity: 1; animation: slideUp 0.5s ease-out; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

        /* --- PREMIUM HEADER BLOCK STYLING --- */
        .header-block { margin-bottom: 2.5rem; padding: 1rem 0; border-bottom: 1px solid #e2e8f0; }
        .header-kicker { color: #C49A23; font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 0.75rem; display: block; }
        .header-main-title { font-size: 2.6rem; font-weight: 800; color: #0f172a; line-height: 1.1; letter-spacing: -0.03em; border-left: 8px solid #4A0C25; padding-left: 1.5rem; }
        
        h2 { font-size: 1.5rem; font-weight: 700; color: #4A0C25; margin-top: 2.5rem; margin-bottom: 1rem; letter-spacing: -0.01em; }

        /* --- DATA TABLES --- */
        table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 2rem 0; background-color: #ffffff; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
        th { background-color: #0f172a; color: #ffffff; font-weight: 700; text-align: left; padding: 1.1rem 1rem; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; }
        td { padding: 1.1rem 1rem; border-bottom: 1px solid #f1f5f9; color: #334155; font-size: 0.9rem; vertical-align: top; line-height: 1.5; }
        tr:hover td { background-color: #fafbfc; }
        
        p { margin-bottom: 1.5rem; line-height: 1.85; color: #475569; text-align: justify; font-size: 1.05rem; }
        
        .frost-lock { filter: blur(8px); opacity: 0.25; pointer-events: none; user-select: none; }
        .teaser-box { background: #fffbeb; border: 1px solid #fde68a; padding: 1.5rem; border-radius: 8px; color: #92400e; font-weight: 700; font-size: 0.9rem; margin-bottom: 2rem; text-align: center; }

        .insight-highlight { background: linear-gradient(135deg, #fdfcfd 0%, #fff 100%); border-left: 5px solid #C49A23; padding: 1.75rem; margin: 2.5rem 0; font-style: italic; color: #4A0C25; font-weight: 600; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); font-size: 1.1rem; }
        
        .sidebar { background-color: #020617; }
        .nav-item { cursor: pointer; transition: all 0.2s; color: #94a3b8; border-left: 4px solid transparent; }
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
            <div class="header-block"><span class="header-kicker">Strategic Objective 01</span><h1 class="header-main-title">Executive Summary & Strategic Objective</h1></div>
            <p>The global multilayer inductor market operates as a foundational pillar within modern electronic architecture, driven by the absolute necessity for precision radio frequency matching and robust power regulation. Demand is structurally tied to the proliferation of compact, high-density electronic assemblies across advanced mobile, industrial, and automotive platforms. The underlying economic landscape heavily rewards extreme miniaturization and stringent environmental qualification over pure production scale.</p>
            <p>The trajectory of the multilayer inductor sector is fundamentally defined by the transition from volumetric consumer electronics growth toward value-dense automotive and industrial applications. Historically, market expansion relied on the sheer unit scale of smartphone and generic computing device production, which offered reliable but low-margin revenue streams. Contemporary market dynamics, however, indicate that raw unit volumes no longer correlate linearly with revenue generation, as advanced applications require highly specialized, premium-priced components. Consequently, manufacturers that successfully pivot their portfolios toward stringent qualification standards secure disproportionate shares of the expanding industry profit pool.</p>
            <p>Strategic objectives within this evolving landscape demand a precise alignment of manufacturing capabilities with high-growth end markets to mitigate the risks of commoditization. For established market leaders such as TDK Corporation, commercial success relies on leveraging advanced material science to meet the exacting requirements of next-generation mobility and telecommunications protocols. Facilities equipped with cutting-edge process technology must be positioned as critical enablers of this premium strategy, ensuring that the supply chain can proactively support the rigorous demands of automotive original equipment manufacturers and digital infrastructure developers.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 ($Mn)</th><th>2035 ($Mn)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>RF / High-Frequency</td><td>$839.12 (58.0%)</td><td>$1,143.43 (54.1%)</td><td>3.14%</td></tr>
                    <tr><td class="font-bold text-[#C49A23]">Automotive-Qualified</td><td>$132.75 (9.2%)</td><td>$299.60 (14.2%)</td><td class="font-bold text-emerald-600">8.48%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>$474.81 (32.8%)</td><td>$672.22 (31.8%)</td><td>3.54%</td></tr>
                </tbody>
            </table>
            <div class="insight-highlight">Strategic Mandate: The automotive sector's rapid acceleration highlights its emerging role as the primary engine for future value creation across the entire passive component ecosystem.</div>
        </article>

        <article id="ch2" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">Core Market Analysis 02</span><h1 class="header-main-title">Market Core: Global Size, Volume, and Trajectory</h1></div>
            <p>The global multilayer inductor market represents a highly concentrated economic ecosystem where total value is governed by the intersection of aggregate device shipments and individual component complexity. Demand is perpetually driven by the necessity to route complex signals through increasingly dense, miniaturized printed circuit boards within mobility and edge-computing hardware. Sustained revenue expansion therefore requires continuous technological iteration to satisfy the severe spatial limitations and thermal constraints of contemporary hardware architectures.</p>
            <p>The absolute scale is anchored by an immense volume of individual component shipments, which are projected to expand significantly over the forecast horizon. This volume expansion is driven by the increasing electronic content per device across virtually all major hardware categories, successfully counterbalancing the plateauing shipment growth of mature consumer devices like smartphones. The manufacturing base faces immense pressure to scale physical output while strictly maintaining the precise electromagnetic characteristics required by telecommunications and automotive end-users, leaving no margin for quality degradation.</p>
            <p>Volume trajectories demonstrate that while radio frequency and compact ferrite components command the vast majority of physical production, structural demand is shifting toward higher-reliability parts. The market must continuously produce tens of billions of highly reliable, miniaturized components just to fulfill the baseline operational requirements of global wireless networks and electrified vehicular platforms.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 (Bn units)</th><th>2035 (Bn units)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td>Total Volume Demand</td><td>77.00 Bn (100%)</td><td>116.11 Bn (100%)</td><td>4.19%</td></tr>
                    <tr><td>Automotive Units</td><td>3.69 Bn (4.8%)</td><td>7.88 Bn (6.8%)</td><td>7.88%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch3" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">Pricing Pillars 03</span><h1 class="header-main-title">Pricing & Value Dynamics</h1></div>
            <p>Segment economics within the multilayer inductor industry are strictly dictated by the average selling price, which remains highly sensitive to the specific material composition, precision, and operational rating of the manufactured component. The financial viability of manufacturing operations relies heavily on actively protecting these price points against the natural deflationary pressures inherent in mature electronic component supply chains. Maintaining robust operating margins requires relentless innovation in proprietary sintering and layering techniques to continually justify premium pricing architectures to procurement teams.</p>
            <p>Pricing architectures across the industry reveal a distinct, rigid hierarchy based entirely on application criticality and manufacturing difficulty. Automotive-qualified inductors command the highest average selling price due to the exhaustive testing protocols, extended thermal warranties, and stringent reliability standards required for integration into safety-critical vehicle systems. Conversely, standard compact ferrite components face continuous, aggressive pricing pressure due to intense regional competition and the sheer scale of commoditized global production capacity, forcing suppliers into a perpetual race to lower absolute manufacturing costs.</p>
            <table>
                <thead><tr><th>Segment</th><th>2025 ASP ($/unit)</th><th>2035 ASP ($/unit)</th><th>CAGR (%)</th></tr></thead>
                <tbody>
                    <tr><td class="font-bold text-[#C49A23]">Automotive-Qualified</td><td>$0.0360</td><td>$0.0380</td><td>0.54%</td></tr>
                    <tr><td>RF / High-Frequency</td><td>$0.0220</td><td>$0.0210</td><td>-0.46%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch4" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">Device Modeling 04</span><h1 class="header-main-title">Demand Engine: Device-Level Modeling (Smartphones)</h1></div>
            <p>Smartphones and wearable devices constitute the absolute baseline of global multilayer inductor consumption, characterized by massive aggregate device shipments and extreme internal spatial constraints. The primary economic driver for this segment is the continuous, uncompromising requirement for advanced impedance matching and signal filtering within increasingly crowded and thermally limited printed circuit boards. Commercial success in this arena demands that manufacturers master ultra-miniaturization while reliably delivering billions of functionally identical components without interruption.</p>
            <p>The smartphone ecosystem remains the largest single consumer of multilayer inductors, despite a well-documented maturation in the underlying global device shipment growth rates. The vital metric sustaining component demand is the content-per-device multiple, which continues to expand aggressively as original equipment manufacturers integrate complex 5G radio frequency front-ends and sophisticated power management integrated circuits into every handset.</p>
            <div class="teaser-box">🔒 OEM-specific content-per-handset and 6G pre-load multipliers are restricted.</div>
        </article>

        <article id="ch5" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">Mobility Modeling 05</span><h1 class="header-main-title">Demand Engine: Device-Level Modeling (Automotive & EVs)</h1></div>
            <p>The automotive sector represents the most critical frontier for value expansion within the passive component industry, driven entirely by the profound architectural shift toward deep electrification and autonomous navigation. The economic landscape here is defined by stringent safety qualifications, harsh operating environments, and zero-defect mandates, which inherently support elevated, highly defensible pricing structures. Component suppliers must prioritize absolute reliability and rigorous lot traceability to penetrate and secure long-term, lucrative positions within modern vehicular supply chains.</p>
            <p>Electric vehicles and advanced driver-assistance systems necessitate a massive, unprecedented increase in the sheer quantity of passive electronic components per chassis. The transition from traditional internal combustion engines to electrified powertrains introduces complex battery management systems, high-voltage traction inverters, and sophisticated in-vehicle infotainment networks, all of which require highly specialized multilayer inductors. These automotive-grade components must exhibit exceptional thermal stability, often rated up to 165°C, and robust resistance to constant mechanical vibration.</p>
        </article>

        <article id="ch17" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">Geopolitics 17</span><h1 class="header-main-title">Trade, Import-Export & Tariff Analysis</h1></div>
            <p>The international trade of multilayer inductors is increasingly subjected to the severe friction of aggressive geopolitical policy, structurally altering the landed costs of electronic components worldwide. The market economics are no longer dictated solely by raw manufacturing efficiency; they are heavily distorted by the sudden imposition of retaliatory tariffs, sweeping import restrictions, and national security embargoes. Successfully navigating this hostile landscape requires highly agile, localized supply chains capable of legally bypassing punitive border taxation.</p>
            <table>
                <thead><tr><th>Country / Region</th><th>Premium Factor</th><th>Regional Multiplier</th><th>Combined Multiplier</th></tr></thead>
                <tbody>
                    <tr><td>United States</td><td>1.10</td><td>1.08</td><td>1.188</td></tr>
                    <tr><td>Vietnam (ASEAN)</td><td>0.88</td><td>0.95</td><td>0.836</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch19" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">TDK Positioning 19</span><h1 class="header-main-title">TDK Strategy: Win/Loss Matrix</h1></div>
            <p>TDK Corporation operates from a highly advantageous, deeply entrenched position within the global passive component ecosystem, uniquely capable of dictating market trends rather than merely reacting to them. The corporate economic strategy relies on leveraging an exceptionally broad technological portfolio and an unmatched historical pedigree in magnetic material science to secure premium market access worldwide. To absolutely dominate the future landscape, the organization must ruthlessly prioritize segments that heavily reward complex engineering over those that merely demand high-volume price matching.</p>
            <p>The win/loss matrix for TDK is distinctly defined by application criticality and the necessity for flawless reliability. TDK holds a massive competitive advantage ("Win") in arenas requiring multi-disciplinary engineering, such as automotive Power-over-Coax networks, high-temperature in-vehicle networking, and comprehensive power management modules. The sheer breadth of their portfolio ensures deep, exceptionally sticky relationships with top-tier automotive and industrial original equipment manufacturers who demand single-source reliability.</p>
            <div class="insight-highlight">"TDK’s most defensible, highly profitable market position resides squarely at the intersection of rigorous automotive qualification and advanced RF capability, distancing the firm from pure scale-driven competition."</div>
        </article>

        <article id="ch20" class="chapter-content max-w-5xl mx-auto">
            <div class="header-block"><span class="header-kicker">The Roadmap 20</span><h1 class="header-main-title">Final Recommendations & Investment Roadmap</h1></div>
            <p>The culmination of this exhaustive market analysis demands a highly focused, uniquely aggressive deployment of corporate capital to capture the most lucrative segments of the evolving multilayer inductor landscape. The core economic reality is that raw unit volume is no longer the primary engine of corporate profitability; absolute value is now generated almost exclusively through extreme miniaturization, harsh-environment qualification, and deep architectural integration into next-generation radio frequency modules. Organizations that fail to immediately align their investment roadmaps with these structural truths will face severe, irreversible margin compression.</p>
            <p>The immediate, non-negotiable investment priority must be the relentless expansion of automotive-qualified (AEC-Q200) production capacity and the highly accelerated commercialization of sub-0402 radio frequency architectures. Capital must be aggressively diverted toward advanced material science—specifically, high-temperature dielectrics and ultra-low-loss ceramics—to support the rigorous, uncompromising demands of electric vehicle traction inverters, advanced driver-assistance networks, and 5G/6G millimeter-wave telecommunications. Concurrently, massive investments in manufacturing automation and yield-optimization software must be executed to protect the baseline profitability of the mature compact ferrite portfolio against intense regional competition.</p>
            <div class="teaser-box">🔒 Chapter 20 Roadmap: NPV and ROI modeling for Ouchi and Akita facility upgrades Restricted.</div>
        </article>

        </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const numChapters = 20;
            const navContainer = document.getElementById('sidebar-nav');
            const chapters = document.querySelectorAll('.chapter-content');
            
            const titles = [
                "Executive Summary", "Global Size & Volume", "Pricing Dynamics", "Smartphones & Wearables",
                "Automotive & EVs", "IoT Edge Modules", "Use-Case Expansion", "Product Benchmarking",
                "Regional: N. America", "Regional: Europe", "Regional: APAC", "Market Share Control",
                "Murata & Samsung", "Regional Challengers", "Value Chain & Profits", "Capacity & Footprint",
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

# Dynamic Replacements
final_html = RAW_HTML_CONTENT.replace("__LOGO_PLACEHOLDER__", html_logo)

# Render HTML inside Streamlit
components.html(final_html, height=880, scrolling=True)
