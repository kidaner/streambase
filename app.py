import pandas as pd
import streamlit as st


st.set_page_config(page_title="playbook",
                   page_icon=":notebook:",
                   layout="wide")

df = pd.read_excel(io="latest.xlsx",
                   engine="openpyxl",
                   sheet_name="latest")

st.dataframe(df)

st.sidebar.header("Filter Results:")

category = st.sidebar.multiselect("Select category:", options=df["Category"].unique(),
                                  default=df["Category"].unique())
