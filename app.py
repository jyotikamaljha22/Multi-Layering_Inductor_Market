import streamlit as st
import plotly.graph_objects as go
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
# THEME TOGGLE
# -----------------------------
theme = st.sidebar.toggle("Dark Mode")

if theme:
    bg = "#0E1117"
    text = "white"
else:
    bg = "#FFFFFF"
    text = "#000000"

st.markdown(f"""
<style>
body {{
    background-color: {bg};
    color: {text};
}}
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
            st.rerun()
        else:
            st.error("Incorrect password")

    st.markdown('</div>', unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    login()
    st.stop()

# -----------------------------
# NAVIGATION
# -----------------------------
chapters = [f"Chapter {i}" for i in range(1,21)]

if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = chapters[0]

selected = st.sidebar.radio("Navigate", chapters)

# -----------------------------
# SCENARIO
# -----------------------------
scenario = st.sidebar.selectbox(
    "Scenario",
    ["Base Case", "Upside", "Downside"]
)

def get_data():
    if scenario == "Base Case":
        return [1446,1727,2115]
    elif scenario == "Upside":
        return [1578,1885,2308]
    else:
        return [1305,1558,1908]

# -----------------------------
# PRESENTATION MODE
# -----------------------------
presentation = st.sidebar.toggle("Presentation Mode")

if presentation:
    st.markdown(f"""
    <div style='background:#5B0F2E;padding:50px;border-radius:20px;color:white;text-align:center;animation: fadeIn 0.6s;'>
        <h1>{selected}</h1>
        <p>Scenario: {scenario}</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# ANIMATED CHART (PLOTLY)
# -----------------------------
def animated_market_chart():
    years = [2025,2030,2035]
    revenue = get_data()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years,
        y=revenue,
        mode='lines+markers',
        line=dict(width=4),
    ))

    fig.update_layout(
        title=f"Market Growth ({scenario})",
        template="plotly_dark" if theme else "plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# SEGMENT CHART
# -----------------------------
def segment_chart():
    fig = go.Figure(data=[
        go.Bar(name='RF', x=["2025","2030","2035"], y=[839,973,1143]),
        go.Bar(name='Ferrite', x=["2025","2030","2035"], y=[474,560,672]),
        go.Bar(name='Auto', x=["2025","2030","2035"], y=[132,193,299]),
    ])

    fig.update_layout(
        barmode='stack',
        title="Segment Evolution",
        template="plotly_dark" if theme else "plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# SCENARIO CHART
# -----------------------------
def scenario_chart():
    fig = go.Figure(data=[
        go.Bar(x=["Base","Upside","Downside"], y=[2115,2308,1908])
    ])

    fig.update_layout(
        title="Scenario Comparison",
        template="plotly_dark" if theme else "plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

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
# CONTENT
# -----------------------------
if selected == "Chapter 1":
    st.markdown("# Executive Summary")

    revenue = get_data()

    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Market 2035", f"${revenue[-1]}Mn")
    col2.metric("CAGR", "3.87%")
    col3.metric("TDK Position", "$318Mn")
    col4.metric("Growth Driver", "Automotive")

    st.markdown("Market driven by RF complexity and automotive expansion.")

    animated_market_chart()
    generate_pdf()

elif selected == "Chapter 4":
    st.markdown("# Segmentation")
    segment_chart()

elif selected == "Chapter 11":
    st.markdown("# Competitive Landscape")

    st.dataframe({
        "Player":["Player 1","Player 2","Player 3","Player 4"],
        "Share":[28,21,10,8]
    })

elif selected == "Chapter 18":
    st.markdown("# Scenario Analysis")
    scenario_chart()

else:
    st.markdown(f"# {selected}")
    st.markdown("Full structured content here.")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
---
**Confidential & Proprietary**  
© 2026 Strategic Market Research  

To access full report: info@strategicmarketresearch.com
""")
