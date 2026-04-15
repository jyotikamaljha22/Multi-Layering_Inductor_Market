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
    page_title="Strategic Market Research | TDK Corporation Advisory",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed", 
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
    .stTextInput input {{
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        padding: 12px 14px !important;
        background: #ffffff !important;
        color: #1e293b !important;
        font-weight: 500 !important;
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

# ----------------------------
# ACCESS CONTROL (CENTERED GATEWAY)
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
        .frost-lock { filter: blur(6px); opacity: 0.3; pointer-events: none; user-select: none; }
        .teaser-banner { background: #fffbeb; border: 1px solid #fde68a; padding: 1rem; border-radius: 8px; color: #92400e; font-weight: 600; font-size: 0.85rem; margin-top: -1.5rem; margin-bottom: 2rem; display: flex; align-items: center; gap: 8px; }

        /* Insight Box */
        .insight-highlight { background: linear-gradient(135deg, #fdfcfd 0%, #fff 100%); border-left: 5px solid #C49A23; padding: 1.5rem; margin: 2rem 0; font-style: italic; color: #4A0C25; font-weight: 600; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
        
        /* Sidebar Navigation */
        .sidebar { background-color: #2D0716; }
        .nav-item { cursor: pointer; transition: all 0.2s; color: #d1d5db; border-left: 4px solid transparent; }
        .nav-item:hover { background-color: rgba(255,255,255,0.05); color: #ffffff; }
        .nav-item.active { background-color: rgba(255,255,255,0.1); color: #C49A23; font-weight: 700; border-left: 4px solid #C49A23; }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
    </style>
</head>
<body class="flex h-screen overflow-hidden">

    <aside class="w-80 sidebar text-slate-300 flex flex-col h-full overflow-y-auto shrink-0 shadow-2xl z-20">
        <div class="p-8 border-b border-white/10 sticky top-0 sidebar">
            <div class="mb-4">__LOGO_PLACEHOLDER__</div>
            <div class="text-xs font-bold tracking-widest text-[#C49A23] uppercase mb-1">Strategic Market Research</div>
            <h2 class="text-xl font-extrabold text-white leading-tight">Multilayer Inductor <br>Boardroom Playbook</h2>
            <div class="text-xs text-slate-400 mt-2 font-medium">TDK Corporation Advisory</div>
        </div>
        <nav class="flex-1 py-4" id="sidebar-nav"></nav>
        <div class="p-6 border-t border-white/10 text-[10px] text-slate-500 uppercase tracking-widest bg-black/20">
            Confidential & Proprietary<br>&copy; 2026 SMR Group
        </div>
    </aside>

    <main class="flex-1 overflow-y-auto bg-slate-50 relative p-8 md:p-12 lg:p-20 scroll-smooth" id="main-content">
        
        <article id="ch1" class="chapter-content active max-w-5xl mx-auto">
            <h1>1. Executive Summary & Strategic Objective</h1>
            <p>The global multilayer inductor market is at a critical inflection point, transitioning from a reliance on consumer electronics volumes toward high-value, reliability-critical applications in Automotive and RF infrastructure. For TDK Corporation, success relies on leveraging advanced material science to bypass the commoditization trap currently affecting legacy compact ferrite lines.</p>
            <div class="insight-highlight">Strategic Mandate: Pivot portfolio weighting toward AEC-Q200 Grade 0 components to capture a projected $299.6M automotive value pool by 2035.</div>
            <table>
                <thead>
                    <tr><th>Segment</th><th>2025 ($Mn)</th><th>2035 ($Mn)</th><th>CAGR (%)</th></tr>
                </thead>
                <tbody>
                    <tr><td>RF / High-Frequency</td><td>$839.12</td><td>$1,143.43</td><td>3.14%</td></tr>
                    <tr><td>Automotive-Qualified</td><td>$132.75</td><td>$299.60</td><td>8.48%</td></tr>
                    <tr><td>Compact Ferrite / NFC</td><td>$474.81</td><td>$672.22</td><td>3.54%</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch2" class="chapter-content max-w-5xl mx-auto">
            <h1>2. Market Core: Global Size & Volume</h1>
            <p>Analysis confirms that unit shipments (Bn units) are decoupled from revenue growth. Manufacturers face a "Volume-Value Scissors" where physical output must expand at 5.5% CAGR to sustain a 3.8% revenue CAGR, driven by ASP erosion in the consumer core.</p>
            <table>
                <thead>
                    <tr><th>Metric</th><th>2025</th><th>2030</th><th>2035</th></tr>
                </thead>
                <tbody>
                    <tr><td>Revenue Pool ($Mn)</td><td>$1,446.68</td><td>$1,727.53</td><td>$2,115.25</td></tr>
                    <tr><td>Volume Load (Bn units)</td><td>85.39</td><td>112.51</td><td>146.40</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch3" class="chapter-content max-w-5xl mx-auto">
            <h1>3. Pricing & Value Dynamics</h1>
            <p>ASP hierarchies are rigid. Automotive parts command a 3x premium over IoT components. TDK must utilize proprietary sintering to defend the $0.022 RF benchmark as regional challengers attempt to bridge the gap from the $0.013 ferrite baseline.</p>
            <table>
                <thead>
                    <tr><th>Segment</th><th>2025 ASP ($/unit)</th><th>2035 ASP ($/unit)</th><th>Pricing Trend</th></tr>
                </thead>
                <tbody>
                    <tr><td>Automotive-Qualified</td><td>$0.0360</td><td>$0.0380</td><td class="text-emerald-600 font-bold">Appreciating</td></tr>
                    <tr><td>RF / High-Frequency</td><td>$0.0220</td><td>$0.0210</td><td class="text-rose-600">Deflationary</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch4" class="chapter-content max-w-5xl mx-auto">
            <h1>4-6. Demand Engines: Device-Level Modeling</h1>
            <p>Smartphones provide the volumetric floor, but Electric Vehicles (EVs) act as the value engine. By 2035, EV component density will reach ~140 units per chassis, fundamentally altering TDK’s shipment mix.</p>
            <div class="teaser-banner"><span>🔒</span> 2,000+ Row Named Project Database Hidden.</div>
            <table class="frost-lock">
                <thead><tr><th>OEM</th><th>Project Name</th><th>Units/Year</th><th>Value</th></tr></thead>
                <tbody>
                    <tr><td>[REDACTED]</td><td>Project Titan</td><td>1.2 Bn</td><td>$$$</td></tr>
                    <tr><td>[REDACTED]</td><td>Giga Chassis V</td><td>0.9 Bn</td><td>$$$</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch5" class="chapter-content max-w-5xl mx-auto">
            <h1>7-8. Use-Cases & Miniaturization Moats</h1>
            <p>01005 (imperial) architectures serve as the definitive tech barrier. Challengers like Sunlord and YAGEO are currently yield-locked at 0201, leaving TDK and Murata as the exclusive suppliers for next-gen 6G modules.</p>
            <table>
                <thead><tr><th>Size (Imperial)</th><th>Tech Barrier</th><th>Yield Stability</th><th>Status</th></tr></thead>
                <tbody>
                    <tr><td>0201 / 0603</td><td>Medium</td><td>98%</td><td>Mass Commodity</td></tr>
                    <tr><td>01005 / 0402</td><td>Extreme</td><td>82%</td><td>Strategic Moat</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch6" class="chapter-content max-w-5xl mx-auto">
            <h1>9-11. Regional Deep Dives (US, EU, APAC)</h1>
            <p>Revenue growth is highest in India (6.5% CAGR) due to localization mandates. China remains the volume anchor but exhibits the highest risk of "Mother-Factory" IP leakage to domestic players.</p>
            <table>
                <thead><tr><th>Region</th><th>2025 Rev ($Mn)</th><th>2035 Rev ($Mn)</th><th>Priority</th></tr></thead>
                <tbody>
                    <tr><td>United States</td><td>$146.58</td><td>$214.84</td><td>Tier 1 (Design)</td></tr>
                    <tr><td>Germany</td><td>$43.63</td><td>$65.76</td><td>Tier 1 (Auto)</td></tr>
                    <tr><td>India</td><td>$134.42</td><td>$253.32</td><td>Tier 2 (Scale)</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch7" class="chapter-content max-w-5xl mx-auto">
            <h1>12-14. Competitive Share & Challenger Analysis</h1>
            <p>The Japanese oligopoly (Murata, TDK) still controls >50% share, but regional challengers are moving up the AEC-Q200 curve. Samsung EM is aggressively bridging from consumer MLCCs into Inductor niches.</p>
            <div class="teaser-banner"><span>🔒</span> Granular Net Profit Margin Comparison Masked.</div>
            <table class="frost-lock">
                <thead><tr><th>Company</th><th>Gross Margin</th><th>Op Margin</th><th>Yield Index</th></tr></thead>
                <tbody>
                    <tr><td>Murata</td><td>[LOCKED]</td><td>[LOCKED]</td><td>Elite</td></tr>
                    <tr><td>Sunlord</td><td>[LOCKED]</td><td>[LOCKED]</td><td>Medium</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch8" class="chapter-content max-w-5xl mx-auto">
            <h1>15-17. Value Chain, Capacity & Geopolitics</h1>
            <p>US Section 122 and IEEPA ad valorem duties permanently distort landed costs. Vietnam (ASEAN) emerges as the vital "Tariff Bypass" node for TDK’s global supply chain resilience.</p>
            <table>
                <thead><tr><th>Geography</th><th>Premium Factor</th><th>Combined Multiplier</th><th>2035 Implication</th></tr></thead>
                <tbody>
                    <tr><td>United States</td><td>1.10</td><td>1.188</td><td>Max Landed Cost</td></tr>
                    <tr><td>Vietnam</td><td>0.88</td><td>0.836</td><td>ASEAN Growth / Bypass</td></tr>
                </tbody>
            </table>
        </article>

        <article id="ch9" class="chapter-content max-w-5xl mx-auto">
            <h1>18-20. Strategic Scenarios & TDK Playbook</h1>
            <p>The "Upside Case" ($2.31Bn) depends on hyper-acceleration of 6G test-beds. TDK's win-zone is identified as Power-over-Coax (PoC) networks for Level 4 Autonomous modules.</p>
            <div class="insight-highlight">"TDK must treat its Ouchi and Akita mother-factories as specialized capability anchors, intentionally abandoning low-ground volume wars to dominate the specialized intersection of mobility and connectivity."</div>
            <div class="teaser-banner"><span>🔒</span> Chapter 20: 10-Year Capex & ROI Roadmap Locked.</div>
        </article>

    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const numChapters = 9; // Grouped for UI brevity in teaser
            const navContainer = document.getElementById('sidebar-nav');
            const chapters = document.querySelectorAll('.chapter-content');
            
            const titles = [
                "Executive Summary & Objectives",
                "Market Core & Volume",
                "Pricing & Value dynamics",
                "Demand Engines & Project Pipeline",
                "Tech Moats & Miniaturization",
                "Regional Analysis & Hotspots",
                "Competitive Control & Share",
                "Value Chain & Geopolitics",
                "Strategic Playbook & ROI"
            ];

            // Generate Nav
            for (let i = 1; i <= numChapters; i++) {
                const navItem = document.createElement('div');
                navItem.className = "nav-item px-8 py-3.5 text-xs font-bold uppercase tracking-widest";
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

# Dynamic Replacement
final_html = RAW_HTML_CONTENT.replace("__LOGO_PLACEHOLDER__", html_logo)

# Render HTML inside Streamlit container
components.html(final_html, height=850, scrolling=True)
