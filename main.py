import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

st.set_page_config(page_title="DataStatPro Clone", layout="wide")
st.markdown("""
<style>
/* Make the app look cleaner and more modern */
body {
    background-color: #f7f9fc;
}
.sidebar .sidebar-content {
    background-color: #004466;
    color: white;
}
.sidebar .sidebar-content .block-container {
    padding: 1rem;
}
.css-1d391kg {
    background-color: #004466;
    color: white;
}
.stButton>button {
    background-color: #006699;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
}
.stButton>button:hover {
    background-color: #005580;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* Import Google font */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

/* Apply the font */
html, body, [class*="css"] {
    font-family: 'Roboto', sans-serif;
    background-color: #f6f9fc;
    color: #1a1a1a;
}

/* Sidebar style */
.sidebar .sidebar-content {
    background-color: #003366;
    padding: 20px;
    color: white;
}

/* Heading styling */
h1, h2, h3 {
    color: #003366;
}

/* Button styling */
.stButton > button {
    background-color: #0072b1;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #005a8c;
}

/* Navbar styling */
.navbar {
    background-color: #003366;
    padding: 15px;
    color: white;
    font-size: 22px;
    font-weight: bold;
}
.navbar a {
    color: white;
    margin-left: 20px;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="navbar">
    DataStatPro Clone
    <a href='#home'>Home</a>
    <a href='#upload'>Upload</a>
    <a href='#analysis'>Analysis</a>
    <a href='#export'>Export</a>
</div>
""", unsafe_allow_html=True)

# Simulated top navigation bar
st.markdown("""
<style>
.navbar {
    background-color: #004466;
    padding: 10px;
    color: white;
    font-size: 24px;
    font-weight: bold;
}
.navbar a {
    color: white;
    margin-right: 15px;
    text-decoration: none;
}
</style>
<div class="navbar">
    DataStatPro Clone
    <a href='#home'>Home</a>
    <a href='#upload'>Upload</a>
    <a href='#analysis'>Analysis</a>
    <a href='#export'>Export</a>
</div>
""", unsafe_allow_html=True)

st.write("")

# Sidebar menu for navigation
menu = st.sidebar.selectbox("Menu", ["Home", "Upload Data", "Analysis", "Export Results"])

if "df" not in st.session_state:
    st.session_state.df = None

if menu == "Home":
    st.title("Welcome to DataStatPro Clone")
    st.write("""
        This app lets you upload your data and perform simple economic/financial analyses.
        Use the sidebar to navigate between pages.
    """)
