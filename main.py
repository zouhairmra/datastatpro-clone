import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
from PIL import Image

st.set_page_config(page_title="DataStatPro Clone", layout="wide")

# Load and show logo
logo = Image.open("logo.png")
st.sidebar.image(logo, width=200)

# Apply custom styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Roboto', sans-serif;
    background-color: #f6f9fc;
    color: #1a1a1a;
}
.sidebar .sidebar-content {
    background-color: #003366;
    padding: 20px;
    color: white;
}
h1, h2, h3 {
    color: #003366;
}
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

# Navbar
st.markdown("""
<div class="navbar">
    DataStatPro Clone
    <a href='#home'>Home</a>
    <a href='#upload'>Upload</a>
    <a href='#analysis'>Analysis</a>
    <a href='#export'>Export</a>
</div>
""", unsafe_allow_html=True)

# Sidebar
menu = st.sidebar.selectbox("Menu", ["Home", "Upload Data", "Analysis", "Export Results"])
if "df" not in st.session_state:
    st.session_state.df = None

# Pages
if menu == "Home":
    st.title("Welcome to DataStatPro Clone")
    st.write("This app lets you upload your data and perform basic analysis.")

elif menu == "Upload Data":
    st.title("Upload your data")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.session_state.df = df
            st.success("Upload successful!")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error: {e}")

elif menu == "Analysis":
    st.title("Data Analysis")
    if st.session_state.df is None:
        st.warning("Upload data first.")
    else:
        df = st.session_state.df
        st.dataframe(df.head())
        analysis = st.selectbox("Choose analysis", [
            "Descriptive Statistics",
            "Correlation Matrix",
            "Linear Regression",
            "Multiple Linear Regression",
            "Histogram",
            "Scatter Plot",
            "Time Series Line Chart"
        ])
        if analysis == "Descriptive Statistics":
            st.dataframe(df.describe())

        elif analysis == "Correlation Matrix":
            corr = df.corr()
            st.dataframe(corr)
            st.plotly_chart(px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', origin='lower'), use_container_width=True)

        elif analysis == "Linear Regression":
            numeric = df.select_dtypes(include="number").columns.tolist()
            y = st.selectbox("Y variable", numeric)
            x = st.selectbox("X variable", [i for i in numeric if i != y])
            if st.button("Run Regression"):
                X = sm.add_constant(df[[x]])
                model = sm.OLS(df[y], X).fit()
                st.write(model.summary())
                st.plotly_chart(px.scatter(df, x=x, y=y, trendline="ols"), use_container_width=True)

        elif analysis == "Multiple Linear Regression":
            numeric = df.select_dtypes(include="number").columns.tolist()
            y = st.selectbox("Y variable", numeric, key="mlr_y")
            x_vars = st.multiselect("X variables", [i for i in numeric if i != y], key="mlr_x")
            if st.button("Run MLR"):
                if x_vars:
                    X = sm.add_constant(df[x_vars])
                    model = sm.OLS(df[y], X).fit()
                    st.write(model.summary())
                else:
                    st.warning("Select at least one X variable.")

        elif analysis == "Histogram":
            col = st.selectbox("Column", df.select_dtypes(include="number").columns)
            st.plotly_chart(px.histogram(df, x=col), use_container_width=True)

        elif analysis == "Scatter Plot":
            numeric = df.select_dtypes(include="number").columns.tolist()
            x = st.selectbox("X axis", numeric, key="scatter_x")
            y = st.selectbox("Y axis", numeric, key="scatter_y")
            st.plotly_chart(px.scatter(df, x=x, y=y), use_container_width=True)

        elif analysis == "Time Series Line Chart":
            time_col = st.selectbox("Time column", df.columns)
            value_col = st.selectbox("Value column", df.select_dtypes(include="number").columns)
            try:
                df[time_col] = pd.to_datetime(df[time_col])
                st.plotly_chart(px.line(df.sort_values(time_col), x=time_col, y=value_col), use_container_width=True)
            except Exception as e:
                st.error(f"Time series plot failed: {e}")

elif menu == "Export Results":
    st.title("Export Data")
    if st.session_state.df is not None:
        csv = st.session_state.df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", data=csv, file_name="dataset.csv", mime="text/csv")
