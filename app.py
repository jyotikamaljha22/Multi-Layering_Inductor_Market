import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# ================================
# CONFIG
# ================================
st.set_page_config(layout="wide")

PASSWORD = "SMR2026"

# ================================
# SESSION STATE
# ================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "1. Executive Summary"

# ================================
# CSS (CLEAN + PREMIUM)
# ================================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

body {
    background-color: #F5F1F3;
}

h1, h2, h3 {
    color: #5B0F2E;
}

.stButton>button {
    background-color: #5B0F2E;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ================================
# LOGIN
# ================================
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
        if password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Incorrect password")

    st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    login()
    st.stop()

# ================================
# NAVIGATION
# ================================
chapters = [
    "1. Executive Summary",
    "2. Market Definition",
    "3. TAM Forecast",
    "4. Segmentation",
    "5. Demand Engine",
    "7. Pricing",
    "11. Competitive Landscape",
    "18. Scenarios",
    "20. Strategy"
]

st.sidebar.title("SMR Dashboard")
selected = st.sidebar.radio("Navigation", chapters, key="nav_choice")

# ================================
# CHARTS
# ================================
def chart_market():
    years = [2025, 2030, 2035]
    revenue = [1446, 1727, 2115]
    volume = [85, 112, 146]

    fig, ax1 = plt.subplots()

    ax1.bar(years, revenue)
    ax1.set_ylabel("Revenue ($Mn)")

    ax2 = ax1.twinx()
    ax2.plot(years, volume, marker='o')
    ax2.set_ylabel("Volume")

    st.pyplot(fig)

def chart_segment():
    years = ["2025","2030","2035"]
    rf = [839,973,1143]
    ferrite = [474,560,672]
    auto = [132,193,299]

    fig, ax = plt.subplots()

    ax.bar(years, rf, label="RF")
    ax.bar(years, ferrite, bottom=rf, label="Ferrite")

    bottom2 = [rf[i]+ferrite[i] for i in range(3)]
    ax.bar(years, auto, bottom=bottom2, label="Auto")

    ax.legend()
    st.pyplot(fig)

# ================================
# PAGES
# ================================

if selected == "1. Executive Summary":
    st.title("Executive Summary")

    st.write("Market is shifting toward automotive premiumization.")

    chart_market()

elif selected == "3. TAM Forecast":
    st.title("TAM Forecast")

    st.write("Growth driven by device density.")

    chart_market()

elif selected == "4. Segmentation":
    st.title("Segmentation")

    st.write("Automotive growing fastest.")

    chart_segment()

elif selected == "7. Pricing":
    st.title("Pricing Dynamics")

    df = pd.DataFrame({
        "Year":[2025,2030,2035],
        "ASP":[0.016,0.015,0.014]
    })

    st.line_chart(df.set_index("Year"))

elif selected == "11. Competitive Landscape":
    st.title("Competitive Landscape")

    df = pd.DataFrame({
        "Player":["Player 1","Player 2","Player 3"],
        "Share":[30,22,9]
    })

    st.bar_chart(df.set_index("Player"))

elif selected == "18. Scenarios":
    st.title("Scenarios")

    df = pd.DataFrame({
        "Year":[2025,2030,2035],
        "Base":[1446,1727,2115],
        "Upside":[1500,1850,2300],
        "Downside":[1300,1550,1900]
    })

    st.line_chart(df.set_index("Year"))

elif selected == "20. Strategy":
    st.title("Strategy")

    st.write("Focus on automotive + RF premium.")

# ================================
# NEXT / PREVIOUS (FIXED)
# ================================
idx = chapters.index(selected)

col1, col2 = st.columns(2)

with col1:
    if idx > 0:
        if st.button("⬅ Previous"):
            st.session_state["nav_choice"] = chapters[idx - 1]
            st.rerun()

with col2:
    if idx < len(chapters) - 1:
        if st.button("Next ➡"):
            st.session_state["nav_choice"] = chapters[idx + 1]
            st.rerun()

# ================================
# FOOTER
# ================================
st.markdown("""
---
**Confidential & Proprietary**  
© 2026 Strategic Market Research  

To access the full report:  
info@strategicmarketresearch.com
""")
