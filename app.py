import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(layout="wide")

# -----------------------------
# BRAND COLORS
# -----------------------------
BURGUNDY = "#5B0F2E"
BG_LIGHT = "#F6F2F4"
WHITE = "#FFFFFF"

# -----------------------------
# THEME
# -----------------------------
dark_mode = st.sidebar.toggle("Dark Mode")

if dark_mode:
    bg = "#0E1117"
    text = "white"
    template = "plotly_dark"
else:
    bg = BG_LIGHT
    text = "#000"
    template = "plotly_white"

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
if "logged" not in st.session_state:
    st.session_state.logged = False

def login():
    st.markdown(f"""
    <div style="background:{BURGUNDY};padding:40px;border-radius:15px;text-align:center;color:white;width:400px;margin:auto;margin-top:120px;">
        <h2>SMR BOARDROOM ACCESS</h2>
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Name")
    pwd = st.text_input("Password", type="password")

    if st.button("Enter"):
        if pwd == "SMR2026":
            st.session_state.logged = True
            st.rerun()
        else:
            st.error("Incorrect password")

if not st.session_state.logged:
    login()
    st.stop()

# -----------------------------
# NAVIGATION
# -----------------------------
chapters = list(CHAPTERS.keys())

if "nav" not in st.session_state:
    st.session_state.nav = chapters[0]

st.session_state.nav = st.sidebar.radio("Chapters", chapters)

# -----------------------------
# SCENARIO
# -----------------------------
scenario = st.sidebar.selectbox("Scenario", ["Base", "Upside", "Downside"])

def get_market():
    if scenario == "Base":
        return [1446,1727,2115]
    elif scenario == "Upside":
        return [1578,1885,2308]
    else:
        return [1305,1558,1908]

# -----------------------------
# CHARTS
# -----------------------------
def market_chart():
    years = [2025,2030,2035]
    data = get_market()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years,
        y=data,
        mode='lines+markers',
        line=dict(width=4,color=BURGUNDY)
    ))

    fig.update_layout(
        title="Market Growth",
        template=template
    )

    st.plotly_chart(fig, use_container_width=True)

def segment_chart():
    fig = go.Figure(data=[
        go.Bar(name="RF", x=["2025","2030","2035"], y=[839,973,1143]),
        go.Bar(name="Ferrite", x=["2025","2030","2035"], y=[474,560,672]),
        go.Bar(name="Auto", x=["2025","2030","2035"], y=[132,193,299]),
    ])

    fig.update_layout(barmode="stack", template=template, title="Segment Mix")
    st.plotly_chart(fig, use_container_width=True)

def scenario_chart():
    fig = go.Figure(data=[
        go.Bar(x=["Base","Upside","Downside"], y=[2115,2308,1908])
    ])

    fig.update_layout(title="Scenario Comparison", template=template)
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# PRESENTATION MODE
# -----------------------------
presentation = st.sidebar.toggle("Presentation Mode")

if presentation:
    st.markdown(f"""
    <div style="background:{BURGUNDY};padding:50px;border-radius:20px;color:white;text-align:center;">
        <h1>{st.session_state.nav}</h1>
        <p>{scenario} Scenario</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# RENDER CONTENT
# -----------------------------
chapter_html = CHAPTERS[st.session_state.nav]

# Insert charts inside chapters strategically
if "Executive Summary" in st.session_state.nav:
    st.markdown(chapter_html, unsafe_allow_html=True)
    market_chart()

elif "Segmentation" in st.session_state.nav:
    st.markdown(chapter_html, unsafe_allow_html=True)
    segment_chart()

elif "Scenario" in st.session_state.nav:
    st.markdown(chapter_html, unsafe_allow_html=True)
    scenario_chart()

else:
    st.markdown(chapter_html, unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
---
**Confidential & Proprietary**  
© 2026 Strategic Market Research  

To access the full report: info@strategicmarketresearch.com
""")
