import streamlit as st
import pandas as pd

st.markdown("""<style>
.stApp { background: linear-gradient(135deg, #00c6ff, #ffffff); }
</style>""", unsafe_allow_html=True)

st.title("📊 Data Viewer")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())