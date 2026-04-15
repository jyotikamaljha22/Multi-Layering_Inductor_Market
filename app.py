import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -----------------------------------------------------------------------------
# Config and Brand Colour System
# -----------------------------------------------------------------------------
# This dashboard provides an interactive, burgundy‑themed overview of the next
# generation selective BCL‑2 inhibitors market (2025–2035) with a focus on
# InnoCare Pharma and its lead asset mesutoclax.  The design and layout are
# derived from the multilayer inductor dashboard and make extensive use of
# custom CSS for a rich, boardroom feel.  Charts are presented using Plotly
# and interspersed throughout the chapters to break up heavy narrative.

st.set_page_config(
    page_title="Global Selective BCL‑2 Inhibitor Market (2025–2035)",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Brand palette
BURGUNDY       = "#5B0F2E"
BURGUNDY_DARK  = "#431024"
BURGUNDY_LIGHT = "#7A163F"
BURGUNDY_SOFT  = "#F7EEF2"
ROSE           = "#E8C7D5"
INK            = "#0F172A"
SLATE          = "#475569"
SLATE_LIGHT    = "#64748B"
BORDER         = "#E5E7EB"
BG             = "#F6F2F4"
WHITE          = "#FFFFFF"

PRIMARY_PASSWORD = "SMR2026"
CLIENT_NAME = "InnoCare Pharma"

# Anchor used for inserting charts into HTML content.  When the report
# encounters this marker in a chapter, an appropriate plot will be drawn in
# its place.
CHART_ANCHOR = "<!--CHART_ANCHOR-->"

# -----------------------------------------------------------------------------
# Quick metrics for the overview hero.  These values summarise the long
# forecast period and highlight key performance indicators.  The mesutoclax
# revenue reflects projections for 2035.  Growth rates correspond to the
# compound annual growth rate of the overall market.
# -----------------------------------------------------------------------------
QUICK_METRICS = {
    "Market Revenue 2035": "$8,329.63Mn",
    "Global CAGR": "11.45%",
    "Mesutoclax 2035": "$1,845.63Mn",
    "Fastest Growing Indication": "MDS (17.16%)",
}

# -----------------------------------------------------------------------------
# Report content.  All superscripts and internal footnote markers have been
# removed to make the narrative cleaner for client consumption.  Each entry
# corresponds to a chapter or subchapter.  Use raw strings to preserve
# formatting and avoid escaping HTML characters.  For brevity in this example
# only the first few chapters are fully defined; later chapters may be
# abbreviated if necessary.
# -----------------------------------------------------------------------------
CHAPTERS = {
    "1. Introduction and Strategic Context": r'''
<div class="chapter-content">
<h1>1. Introduction and Strategic Context</h1>
<p>The pharmaceutical industry is witnessing a transformative era in the treatment of hematologic malignancies, characterised by the displacement of traditional cytotoxic chemotherapies by highly targeted interventions. At the forefront of this evolution is the apoptosis pathway, specifically therapeutic modulation of the B‑cell lymphoma‑2 (BCL‑2) protein. BCL‑2 is a critical pro‑survival protein that prevents programmed cell death in cancer cells, particularly in B‑cell lineages. The first‑generation selective BCL‑2 inhibitor, venetoclax, has redefined the standard of care in chronic lymphocytic leukemia (CLL) and acute myeloid leukemia (AML), demonstrating the profound commercial and clinical potential of this class.</p>
<p>As the market enters 2025 the competitive landscape is shifting from a single‑product monopoly toward a sophisticated competitive oligopoly. The emergence of next‑generation BCL‑2 inhibitors—including InnoCare Pharma’s mesutoclax (ICP‑248), BeOne’s sonrotoclax (BGB‑11417) and Ascentage Pharma’s lisaftoclax (APG‑2575)—signals a new phase of market maturity. These challengers are designed to improve upon the first‑generation benchmark by offering superior potency, greater selectivity over BCL‑xL (thereby reducing hematologic toxicity) and more predictable pharmacokinetic profiles that may simplify or eliminate the complex dose‑escalation schedules currently required to mitigate tumour lysis syndrome (TLS).</p>
<p>For InnoCare Pharma the strategic imperative centres on navigating the displacement dynamics of a market where venetoclax is deeply entrenched. The objective is not merely to offer a me‑too alternative but to establish mesutoclax as a best‑in‑class asset through superior combination regimens, specifically by leveraging InnoCare’s proprietary BTK inhibitor orelabrutinib to create a unified, client‑controlled fixed‑duration therapy. The forecast period of 2025–2035 represents a critical window during which these next‑generation agents will either displace the incumbent or expand the class into earlier lines of therapy and additional indications like mantle cell lymphoma (MCL) and higher‑risk myelodysplastic syndromes (MDS).</p>
</div>
''',
    "2. Market Segmentation and Forecast Scope": r'''
<div class="chapter-content">
<h1>2. Market Segmentation and Forecast Scope</h1>
<p>The structural architecture of this research is built upon a rigorous definition of the selective BCL‑2 inhibitor space. The core market is strictly confined to small‑molecule BH3 mimetics that demonstrate high selectivity for BCL‑2; this specificity is the primary driver of the favourable safety profile required for combination use. While dual BCL‑2/BCL‑xL inhibitors and MCL‑1 inhibitors are biologically related, they are excluded from the core market sizing due to their distinct toxicity profiles—most notably dose‑limiting thrombocytopenia associated with BCL‑xL inhibition and cardiac safety signals observed with early MCL‑1 candidates.</p>
<p>The segmentation depth follows a multi‑dimensional framework to ensure boardroom precision. Geographically the market is segmented into the United States, China, the EU5 (France, Germany, Italy, Spain and the UK) and the Rest of the World (ROW). China is analysed as a distinct entity because its launch timelines, domestic competitive density and unique reimbursement mechanisms create a commercial environment that differs materially from Western markets.</p>
<p>Indications are categorised by their commercial proof points and developmental risk. CLL/SLL remains the anchor indication, driving over 90&nbsp;percent of class value through 2035. MCL is identified as a high‑value niche for displacement, particularly in the relapsed/refractory setting after BTK inhibitor failure. In the myeloid space AML is the most established expansion indication, while higher‑risk MDS is treated with greater caution following clinical setbacks of the first‑generation class.</p>
</div>
''',
    "3. Core Market Overview": r'''
<div class="chapter-content">
<h1>3. Core Market Overview</h1>
<p>The selective BCL‑2 inhibitor market in 2025 is valued at approximately $2.82&nbsp;billion, a figure predominantly attributed to global sales of venetoclax. These agents work by binding to the hydrophobic BH3‑binding groove of the BCL‑2 protein, which displaces pro‑apoptotic proteins like BIM and BAX, ultimately triggering mitochondrial outer membrane permeabilisation and programmed cell death. This mechanism has proven remarkably effective in lymphoid malignancies, where cancer cells are often primed for apoptosis but held in check by overexpression of BCL‑2.</p>
<p>Despite the success of the first‑generation inhibitor, the current market reveals significant operational friction. Administration of venetoclax in CLL requires a mandatory five‑week dose ramp‑up and intensive laboratory monitoring to prevent TLS. This complexity has historically limited the use of BCL‑2 inhibitors in the community oncology setting, where simpler continuous therapies like BTK inhibitors have maintained dominance.</p>
<p>The next‑generation market is defined by a quest for convenience and safety. Agents like mesutoclax and sonrotoclax are being developed with pharmacokinetic properties that may allow for more rapid dosing or even outpatient initiation without the same intensive monitoring requirements. This shift is essential for expanding class penetration from the 30–40&nbsp;percent range in 2025 to a projected 60–70&nbsp;percent in lymphoid indications by 2035.</p>
</div>
''',
    "4. Market Size and Growth Insights": r'''
<div class="chapter-content">
<h1>4. Market Size and Growth Insights</h1>
<p>The global BCL‑2 inhibitor market is projected to reach $5.14&nbsp;billion by 2030 and expand further to $8.33&nbsp;billion by 2035. This represents a robust long‑term growth trajectory driven by expansion of the addressable patient pool and successful launch of next‑generation challengers. The CLL/SLL segment will remain the dominant engine of growth, increasing from $2.53&nbsp;billion in 2025 to $7.62&nbsp;billion by 2035. Growth is fuelled by both rising incidence of CLL in ageing populations and a shift from continuous monotherapy toward more intensive fixed‑duration combination regimens in the frontline setting.</p>
<p>The growth insights highlight a critical transition in the 2029–2031 period. During this window the entry of sonrotoclax and mesutoclax in the US and EU5 will coincide with the potential plateauing of first‑generation revenue. As venetoclax faces patent expiry and arrival of generics, market value will increasingly migrate toward branded next‑generation assets that can justify premium pricing through superior combination labels and improved safety profiles.</p>
<p>The table below summarises total market revenue by indication; values are millions of USD and cover 2025–2035.</p>
<table>
  <thead>
    <tr>
      <th>Indication</th>
      <th>2025</th>
      <th>2030</th>
      <th>2035</th>
      <th>CAGR</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>CLL/SLL</td><td>2,530.43</td><td>4,677.53</td><td>7,620.25</td><td>11.65%</td></tr>
    <tr><td>MCL</td><td>36.83</td><td>83.70</td><td>135.08</td><td>13.89%</td></tr>
    <tr><td>AML</td><td>214.35</td><td>294.11</td><td>407.25</td><td>6.62%</td></tr>
    <tr><td>MDS</td><td>34.26</td><td>89.30</td><td>167.06</td><td>17.16%</td></tr>
    <tr><td><strong>Global Total</strong></td><td><strong>2,815.87</strong></td><td><strong>5,144.63</strong></td><td><strong>8,329.63</strong></td><td><strong>11.45%</strong></td></tr>
  </tbody>
</table>
</div>
''',
    "5. Key Market Drivers": r'''
<div class="chapter-content">
<h1>5. Key Market Drivers</h1>
<p>The primary driver of the BCL‑2 market’s upward trajectory is regulatory validation and rapid adoption of fixed‑duration all‑oral combination regimens. In 2026 the FDA approved a doublet consisting of acalabrutinib and venetoclax, establishing the first 100&nbsp;percent oral time‑limited regimen for previously untreated CLL patients. This trend is strategically favourable for InnoCare, as it validates the logic of combining a BTK inhibitor with a BCL‑2 inhibitor to achieve deeper remissions while allowing patients a treatment‑free interval.</p>
<p>A second driver is the move toward undetectable minimal residual disease (uMRD) as a surrogate for clinical benefit and a guide for treatment cessation. Evidence from trials such as SEQUOIA and SYMPATICO shows that BTKi plus BCL‑2 combinations drive uMRD rates significantly higher than BCL‑2 monotherapy or BCL‑2 combined with anti‑CD20 antibodies. For payers and clinicians the ability to stop therapy once a patient reaches uMRD represents a functional cure model that reduces long‑term toxicity and financial burden of chronic treatment.</p>
<p>Finally, the increasing incidence of hematologic malignancies due to global population ageing ensures a growing volume of eligible patients. As diagnosis rates improve in regions like China and the Rest of the World, the addressable patient pool for BCL‑2 inhibitors is expected to expand from roughly 230,000 in 2025 to over 290,000 by 2035 across the four core indications.</p>
</div>
''',
    "6. Market Challenges and Restraints": r'''
<div class="chapter-content">
<h1>6. Market Challenges and Restraints</h1>
<p>Despite optimistic growth projections, the market faces significant operational and clinical restraints. The risk of TLS remains the most formidable barrier to broad adoption of the BCL‑2 class. Even with next‑generation assets, memories of severe TLS events in early venetoclax trials continue to influence prescribing behaviour, particularly in community settings where infrastructure for intensive monitoring may be less robust. Any safety signal involving fatal TLS or grade 3/4 neutropenia in pivotal trials for mesutoclax or sonrotoclax could lead to restrictive labelling and slower uptake.</p>
<p>Furthermore, the failure of the VERONA trial in MDS has introduced scepticism regarding the translation of BCL‑2 success from AML to MDS. In MDS the pathophysiology is characterised by a higher degree of clonal complexity and a potentially different reliance on BCL‑2 for survival compared with AML blasts. This failure suggests that next‑generation inhibitors will need to provide compelling overall survival benefits to secure favourable reimbursement and guideline positioning in MDS.</p>
<p>Economic restraints are intensifying. In the United States implementation of the Inflation Reduction Act allows government price negotiations on high‑spend Medicare drugs, which could impact long‑term revenue potential of BCL‑2 inhibitors on the market. In Europe, stringent health technology assessment requirements mean that incremental improvements in safety or convenience may not be sufficient to secure premium pricing unless accompanied by superior progression‑free or overall survival compared with the first‑generation benchmark.</p>
</div>
''',
    # Additional chapters (7–21) have been truncated for brevity.  Follow the same
    # pattern when populating the remaining sections of the report.  You can
    # extend this dictionary with more content or leave empty strings for
    # chapters that do not require display.
    "7. Market Trends and Innovations": r'''
<div class="chapter-content">
<h1>7. Market Trends and Innovations</h1>
<p>A defining trend for the next decade is the accelerated regulatory pathway for domestic hematology assets in China. Innovative Chinese biotechs now compete directly with multinational corporations by utilising China’s Breakthrough Therapy Designation (BTD) to fast‑track approvals. Mesutoclax was the first BCL‑2 inhibitor to receive BTD in China for BTKi‑treated relapsed/refractory MCL, illustrating how local regulatory support can provide a significant time‑to‑market advantage. This trend is not isolated: Ascentage’s lisaftoclax achieved a July 2025 approval in China, establishing a domestic proof of concept for next‑generation BCL‑2 inhibitors.</p>
<p>Technological innovation is moving beyond simple small‑molecule inhibition toward targeted protein degradation. BCL‑2 degraders such as proteolysis‑targeting chimeras (PROTACs) are in early clinical development. These agents recruit the cell’s own waste disposal machinery to eliminate the BCL‑2 protein entirely, rather than simply blocking its active site. This has the potential to overcome point mutations in BCL‑2—such as the G101V mutation—that frequently cause resistance to traditional BH3 mimetics like venetoclax.</p>
<p>Additionally, development of so‑called mutation‑blind inhibitors is gaining traction. As patients are treated with BCL‑2 inhibitors in earlier lines, the emergence of resistant clones becomes a major clinical challenge. Innovation is currently focused on finding molecules that can bind to alternative pockets of the BCL‑2 protein or target upregulation of compensatory pro‑survival proteins like MCL‑1 or BCL‑xL, which often co‑emerge as resistance mechanisms.</p>
</div>
''',
    # other chapters omitted for brevity
    "21.1. Summary of Mesutoclax Opportunity": r'''
<div class="chapter-content">
<h1>21.1. Summary of Mesutoclax Opportunity</h1>
<p>The table below summarises mesutoclax’s opportunity across the forecast period. Revenue is projected to grow from zero in 2025 to $1.85 billion by 2035, driven by both displacement of the incumbent venetoclax and expansion into new indications.</p>
<table>
  <thead><tr><th>Metric</th><th>2025</th><th>2030</th><th>2035</th></tr></thead>
  <tbody>
    <tr><td>Mesutoclax Global Revenue (USD&nbsp;M)</td><td>0.0</td><td>531.12</td><td>1,845.63</td></tr>
    <tr><td>Displacement Value (USD&nbsp;M)</td><td>0.0</td><td>355.22</td><td>1,244.74</td></tr>
    <tr><td>Expansion Value (USD&nbsp;M)</td><td>0.0</td><td>175.90</td><td>600.89</td></tr>
    <tr><td>Market Share (%)</td><td>0.0%</td><td>10.32%</td><td>22.16%</td></tr>
  </tbody>
</table>
</div>
''',
}

# -----------------------------------------------------------------------------
# Confidentiality and sanitisation
# -----------------------------------------------------------------------------
# In this report there are no competitor aliases defined.  Should names need
# anonymisation in the future a mapping can be placed here and applied to
# relevant chapters as in the multilayer inductor example.

# -----------------------------------------------------------------------------
# Data for visuals: revenue by indication, region and scenarios
# -----------------------------------------------------------------------------
indication_df = pd.DataFrame({
    "Indication": ["CLL/SLL", "MCL", "AML", "MDS"],
    "2025": [2530.43, 36.83, 214.35, 34.26],
    "2030": [4677.53, 83.70, 294.11, 89.30],
    "2035": [7620.25, 135.08, 407.25, 167.06],
})

region_df = pd.DataFrame({
    "Region": ["United States", "China", "EU5", "Rest of World"],
    "2025": [1802.09, 48.17, 756.92, 208.68],
    "2030": [3263.15, 106.45, 1401.40, 373.63],
    "2035": [5151.18, 147.12, 2283.62, 747.71],
})

scenario_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Base": [2815.87, 5144.63, 8329.63],
    "Upside": [2950.0, 5600.0, 9000.0],  # illustrative upside
    "Downside": [2600.0, 4700.0, 7600.0],  # illustrative downside
})

mesutoclax_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Revenue": [0.0, 531.12, 1845.63],
})

competitor_df = pd.DataFrame({
    "Competitor": ["Venetoclax", "Mesutoclax", "Sonrotoclax", "Lisaftoclax"],
    "2025": [100.0, 0.0, 0.0, 0.0],
    "2035": [27.5, 22.2, 36.9, 13.4],
})

addressable_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Addressable Patients (k)": [230.0, 260.0, 290.0],
    "Revenue ($Mn)": [2815.87, 5144.63, 8329.63],
})

# -----------------------------------------------------------------------------
# Session State Setup
# -----------------------------------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "visitor_name" not in st.session_state:
    st.session_state.visitor_name = ""
if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "Overview"

# -----------------------------------------------------------------------------
# CSS Injection
# -----------------------------------------------------------------------------
def inject_css(login_mode: bool = False) -> None:
    """
    Inject custom CSS to tailor the appearance of the dashboard.  When
    login_mode is True the sidebar is hidden to focus the user on the
    authentication form.  Colours and spacing reflect the burgundy palette.
    """
    sidebar_login_hide = "section[data-testid='stSidebar'] {display:none !important;}" if login_mode else ""
    st.markdown(
        f"""
        <style>
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
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
                background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_DARK} 72%);
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
                background: linear-gradient(180deg, {BURGUNDY} 0%, {BURGUNDY_DARK} 100%);
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
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# Helper functions for UI components and charts
# -----------------------------------------------------------------------------
def metric_card(label: str, value: str, note: str) -> None:
    """Render a metric card with a label, value and note."""
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
    """Display a section introduction with a title and subtitle."""
    st.markdown(
        f'<div class="section-title">{title}</div><div class="section-subtitle">{subtitle}</div>',
        unsafe_allow_html=True,
    )

def style_plot(fig: go.Figure, title: str, height: int = 360) -> go.Figure:
    """Apply a consistent style to Plotly figures."""
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
    """Return HTML for a chapter title, or a placeholder if missing."""
    return CHAPTERS.get(
        title,
        f"""
        <div class="chapter-content">
            <h1>{title}</h1>
            <p>No content found for this chapter.</p>
        </div>
        """,
    )

def insert_chart_anchor(title: str, html_content: str) -> str:
    """Insert the chart anchor into chapters where inline charts should appear."""
    # We insert the anchor for specific chapters based on the title prefix
    replacements = {
        "4. ": "</table>",       # after the table in chapter 4
        "11. ": "</table>",      # after the table in chapter 11 (regional)
        "21.1": "</table>",      # after the table in summary
    }
    for prefix, marker in replacements.items():
        if title.startswith(prefix) and marker in html_content and CHART_ANCHOR not in html_content:
            return html_content.replace(marker, f"\n{CHART_ANCHOR}\n{marker}", 1)
    return html_content

# -----------------------------------------------------------------------------
# Chart rendering functions for the overview tabs
# -----------------------------------------------------------------------------
def revenue_patients_chart() -> None:
    """Plot market revenue vs. addressable patients over time."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(
        x=addressable_df["Year"], y=addressable_df["Revenue ($Mn)"],
        mode="lines+markers", name="Revenue ($Mn)",
        line=dict(color=BURGUNDY, width=4), marker=dict(size=10, color=BURGUNDY)
    ), secondary_y=False)
    fig.add_trace(go.Bar(
        x=addressable_df["Year"], y=addressable_df["Addressable Patients (k)"],
        name="Addressable Patients (k)", marker_color="#D7B2C0", opacity=0.78
    ), secondary_y=True)
    fig.update_yaxes(title_text="Revenue ($Mn)", secondary_y=False)
    fig.update_yaxes(title_text="Patients (k)", secondary_y=True)
    style_plot(fig, "Revenue vs. addressable patients", 380)
    st.plotly_chart(fig, use_container_width=True)

def indication_bar_chart() -> None:
    """Show stacked bar chart for revenue by indication."""
    fig = go.Figure()
    fig.add_trace(go.Bar(name="CLL/SLL", x=indication_df["Indication"], y=indication_df["2035"], marker_color=BURGUNDY))
    fig.add_trace(go.Bar(name="MCL", x=indication_df["Indication"], y=indication_df.loc[indication_df["Indication"] == "MCL", "2035"], marker_color="#B07A92"))
    fig.add_trace(go.Bar(name="AML", x=indication_df["Indication"], y=indication_df.loc[indication_df["Indication"] == "AML", "2035"], marker_color="#D7B2C0"))
    fig.add_trace(go.Bar(name="MDS", x=indication_df["Indication"], y=indication_df.loc[indication_df["Indication"] == "MDS", "2035"], marker_color="#E8C7D5"))
    fig.update_layout(barmode="stack")
    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "2035 indication revenue mix", 360)
    st.plotly_chart(fig, use_container_width=True)

def indication_series_chart() -> None:
    """Plot revenue evolution by indication over time."""
    melt = indication_df.melt(id_vars="Indication", var_name="Year", value_name="Revenue")
    fig = px.bar(
        melt, x="Year", y="Revenue", color="Indication", barmode="group",
        color_discrete_sequence=[BURGUNDY, "#B07A92", "#D7B2C0", "#E8C7D5"]
    )
    style_plot(fig, "Revenue by indication (2025–2035)", 380)
    st.plotly_chart(fig, use_container_width=True)

def region_series_chart() -> None:
    """Plot revenue evolution by region over time."""
    melt = region_df.melt(id_vars="Region", var_name="Year", value_name="Revenue")
    fig = px.bar(
        melt, x="Region", y="Revenue", color="Year", barmode="group",
        color_discrete_sequence=[BURGUNDY, "#B07A92", "#D7B2C0"]
    )
    style_plot(fig, "Regional revenue by year", 380)
    st.plotly_chart(fig, use_container_width=True)

def scenario_sensitivity_chart() -> None:
    """Plot scenario sensitivity lines for total market revenue."""
    fig = go.Figure()
    for name, colour in [("Base", BURGUNDY), ("Upside", "#A4456F"), ("Downside", "#D8B5C3")]:
        fig.add_trace(go.Scatter(
            x=scenario_df["Year"], y=scenario_df[name], mode="lines+markers", name=name,
            line=dict(width=4, color=colour), marker=dict(size=9, color=colour)
        ))
    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "Scenario sensitivity (2025–2035)", 360)
    st.plotly_chart(fig, use_container_width=True)

def mesutoclax_growth_chart() -> None:
    """Plot growth of mesutoclax revenue over time."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=mesutoclax_df["Year"], y=mesutoclax_df["Revenue"],
        mode="lines+markers+text", name="Mesutoclax",
        text=[f"${v:.2f}M" for v in mesutoclax_df["Revenue"]], textposition="top center",
        line=dict(color=BURGUNDY_LIGHT, width=4), marker=dict(size=10, color=BURGUNDY_LIGHT)
    ))
    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "Mesutoclax revenue growth", 360)
    st.plotly_chart(fig, use_container_width=True)

def competitor_share_chart() -> None:
    """Plot competitor share in 2025 vs 2035 for key brands."""
    melt = competitor_df.melt(id_vars="Competitor", var_name="Year", value_name="Share")
    fig = px.bar(
        melt, x="Competitor", y="Share", color="Year", barmode="group",
        color_discrete_sequence=[BURGUNDY, "#D7B2C0"]
    )
    style_plot(fig, "Select competitor share comparison", 360)
    st.plotly_chart(fig, use_container_width=True)

# Chart insertion based on chapter titles
def render_inline_chart(title: str) -> None:
    """Render a chart inline depending on the chapter title."""
    if title.startswith("4. "):
        # Market size and growth: show indication series
        indication_series_chart()
    elif title.startswith("11. "):
        # Regional landscape: show region chart
        region_series_chart()
    elif title.startswith("21.1"):
        # Summary of mesutoclax opportunity
        mesutoclax_growth_chart()

# -----------------------------------------------------------------------------
# Rendering functions for overview and chapters
# -----------------------------------------------------------------------------
def render_hero() -> None:
    """Display the hero card with title and subtitle."""
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-kicker">Boardroom Preview Dashboard</div>
            <div class="hero-title">Global Selective BCL‑2 Inhibitor Market (2025–2035)</div>
            <div class="hero-subtitle">Displacement dynamics, combination regimens and strategic positioning for InnoCare</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_overview() -> None:
    """Render the overview page with hero, metrics and tabs."""
    render_hero()
    # Metrics row
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Market Revenue 2035", QUICK_METRICS["Market Revenue 2035"], "Total class value in 2035")
    with c2:
        metric_card("Global CAGR", QUICK_METRICS["Global CAGR"], "2025–2035 base case")
    with c3:
        metric_card("Mesutoclax 2035", QUICK_METRICS["Mesutoclax 2035"], "Projected revenue for mesutoclax")
    with c4:
        metric_card("Fastest Growing Indication", QUICK_METRICS["Fastest Growing Indication"], "Growth leader through 2035")

    st.markdown("")
    tab1, tab2, tab3, tab4 = st.tabs(["Market trajectory", "Value pools", "Regional architecture", "Competition & scenarios"])

    with tab1:
        section_intro("Trajectory and patients", "Market expansion and addressable patient pool over time.")
        revenue_patients_chart()

    with tab2:
        section_intro("Indication mix", "Breakdown of revenue by indication and the 2035 mix.")
        col_a, col_b = st.columns([1.2, 1])
        with col_a:
            indication_series_chart()
        with col_b:
            indication_bar_chart()

    with tab3:
        section_intro("Regional composition", "Evolution of value across major regions.")
        region_series_chart()

    with tab4:
        section_intro("Competitive and scenario view", "Selective competitor share and scenario sensitivity through 2035.")
        col_a, col_b = st.columns([1.05, 1.15])
        with col_a:
            competitor_share_chart()
        with col_b:
            scenario_sensitivity_chart()

        st.markdown("")
        st.markdown(
            """
            <div class="small-callout">
                <div class="section-title" style="margin-bottom:8px;">Executive interpretation</div>
                <div class="section-subtitle" style="margin-bottom:0;">
                    The dashboard illustrates a displacement‑driven narrative: venetoclax dominance gives way to next‑generation entrants, with mesutoclax emerging as a key player through its combination fit and China acceleration.  While CLL/SLL remains the value anchor, MDS displays the highest growth rate, and regional growth leans towards China and the Rest of World.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

def render_chapter_page(title: str) -> None:
    """Render a single chapter page with an optional inline chart."""
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

# -----------------------------------------------------------------------------
# Login and authentication
# -----------------------------------------------------------------------------
def render_login() -> None:
    """Render the login form.  Hides the sidebar during login."""
    inject_css(login_mode=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(
                """
                <h2 style='text-align: center; color: #5B0F2E; padding-bottom: 15px;'>
                    SMR BOARDROOM ACCESS
                </h2>
                """,
                unsafe_allow_html=True,
            )
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

# -----------------------------------------------------------------------------
# Application entry point
# -----------------------------------------------------------------------------
if not st.session_state.authenticated:
    render_login()
    st.stop()

# Normal app after login
inject_css(login_mode=False)

nav_options = ["Overview"] + list(CHAPTERS.keys())

st.sidebar.markdown(
    f"""
    <div class="sidebar-brand">
        <div class="sidebar-kicker">Strategic Market Research</div>
        <div class="sidebar-title">Selective BCL‑2 Inhibitor Market</div>
        <div class="sidebar-sub">Client: {CLIENT_NAME}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f"""
    <div class="sidebar-user">
        Viewing as <strong>{st.session_state.visitor_name}</strong><br>
        Premium preview mode · Executive dashboard
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
    render_chapter_page(st.session_state.nav_choice)
st.markdown('</div>', unsafe_allow_html=True)

import streamlit.components.v1 as components

# Footer on the main page
components.html(
    """
    <div style="
        margin-top: 30px;
        padding: 18px 22px;
        border-radius: 18px;
        background: linear-gradient(135deg, #FAF2F5 0%, #F3E3EA 100%);
        border: 1px solid #E7D3DD;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
        font-family: Inter, sans-serif;
    ">
        <div style="font-size: 13px; color: #5B0F2E; font-weight: 600;">
            Confidential & Proprietary © 2026 Strategic Market Research
        </div>

        <div style="font-size: 13px; color: #7A163F;">
            Access full report:
            <a href="mailto:info@strategicmarketresearch.com"
               style="color:#5B0F2E; font-weight:700; text-decoration:none; margin-left:6px;">
               info@strategicmarketresearch.com
            </a>
        </div>
    </div>
    """,
    height=80,
)
