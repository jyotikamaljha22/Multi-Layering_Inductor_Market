import streamlit as st
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(layout="wide")

# Hide Streamlit UI
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOGIN
# -----------------------------
def login():
    st.markdown("""
    <style>
    .login-box {
        background: linear-gradient(135deg, #5B0F2E, #7A1C3A);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        color: white;
        max-width: 400px;
        margin: auto;
        margin-top: 120px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("## SMR BOARDROOM ACCESS")

    name = st.text_input("Name")
    password = st.text_input("Password", type="password")

    if st.button("Enter"):
        if password == "SMR2026":
            st.session_state.logged_in = True
            st.session_state.user = name
            st.rerun()
        else:
            st.error("Incorrect password")

    st.markdown('</div>', unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    login()
    st.stop()

# -----------------------------
# STATE
# -----------------------------
chapters = [f"Chapter {i}" for i in range(1,21)]

if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = chapters[0]

# Scenario
scenario = st.sidebar.selectbox(
    "Scenario",
    ["Base Case", "Upside", "Downside"]
)
st.session_state.scenario = scenario

# Presentation mode
presentation_mode = st.sidebar.toggle("Presentation Mode")

# -----------------------------
# DATA
# -----------------------------
def get_market_data():
    if scenario == "Base Case":
        return [1446, 1727, 2115]
    elif scenario == "Upside":
        return [1578, 1885, 2308]
    else:
        return [1305, 1558, 1908]

# -----------------------------
# CHARTS
# -----------------------------
def market_chart():
    years = [2025, 2030, 2035]
    revenue = get_market_data()
    volume = [85, 112, 146]

    fig, ax1 = plt.subplots()
    ax1.bar(years, revenue)
    ax2 = ax1.twinx()
    ax2.plot(years, volume, marker='o')

    ax1.set_title(f"Market Outlook ({scenario})")
    st.pyplot(fig)

def segment_chart():
    years = ["2025","2030","2035"]
    rf = [839,973,1143]
    ferrite = [474,560,672]
    auto = [132,193,299]

    fig, ax = plt.subplots()
    ax.bar(years, rf)
    ax.bar(years, ferrite, bottom=rf)
    bottom2 = [rf[i]+ferrite[i] for i in range(3)]
    ax.bar(years, auto, bottom=bottom2)

    ax.set_title("Segment Evolution")
    st.pyplot(fig)

def scenario_chart():
    labels = ["Base","Upside","Downside"]
    values = [2115,2308,1908]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Scenario Comparison")
    st.pyplot(fig)

# -----------------------------
# PDF EXPORT
# -----------------------------
def generate_pdf():
    doc = SimpleDocTemplate("SMR_Report.pdf")
    styles = getSampleStyleSheet()

    content = [
        Paragraph("Global Multilayer Inductor Market", styles['Title']),
        Paragraph(f"Scenario: {scenario}", styles['Normal'])
    ]

    doc.build(content)

    with open("SMR_Report.pdf", "rb") as f:
        st.download_button("Download PDF", f)

# -----------------------------
# NAVIGATION
# -----------------------------
selected = st.sidebar.radio("Navigate", chapters)

# -----------------------------
# PRESENTATION MODE
# -----------------------------
if presentation_mode:
    st.markdown(f"""
    <div style='background:#5B0F2E;padding:40px;border-radius:20px;color:white;text-align:center'>
    <h1>{selected}</h1>
    <p>Scenario: {scenario}</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# CONTENT
# -----------------------------
if selected == "Chapter 1":
    st.markdown("# Executive Summary")

    revenue = get_market_data()
    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Market 2035", f"${revenue[-1]}Mn")
    col2.metric("CAGR", "3.87%")
    col3.metric("TDK Position", "$318Mn")
    col4.metric("Growth Vector", "Automotive")

    st.markdown("Market driven by RF complexity and automotive expansion.")

    market_chart()
    generate_pdf()

elif selected == "Chapter 4":
    st.markdown("# Segmentation")
    st.markdown("Automotive is fastest-growing segment.")
    segment_chart()

elif selected == "Chapter 11":
    st.markdown("# Competitive Landscape")

    players = ["Player 1","Player 2","Player 3","Player 4"]
    shares = [28,21,10,8]

    st.dataframe({"Player":players,"Share":shares})

elif selected == "Chapter 18":
    st.markdown("# Scenario Analysis")
    scenario_chart()

else:
    st.markdown(f"# {selected}")
    st.markdown("Full structured content displayed here.")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
---
**Confidential & Proprietary**  
© 2026 Strategic Market Research  

To access full report: info@strategicmarketresearch.com
""")
