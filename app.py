import pandas as pd
import streamlit as st

# Set the maximum column width to 50 characters
pd.set_option('display.max_colwidth', 50)

# Define a custom theme
st.set_page_config(
    page_title="playbook",
    page_icon=":notebook:",
    layout="wide"
)

df = pd.read_excel(io="latest.xlsx",
                   engine="openpyxl",
                   sheet_name="latest")

# Format the date column to display in the format "2-23"
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%-m-%d")

# Set the maximum column width of the "Text" column to 100 characters
df.style.set_properties(
    subset=["Text"], **{'max-width': '100px', 'text-wrap': 'break-word'})

st.sidebar.header("playbook")

category = st.sidebar.multiselect("Select category:", options=df["Category"].unique(),
                                  default=df["Category"].unique())

label = st.sidebar.multiselect("Select label:", options=df["Label"].unique(),
                               default=df["Label"].unique())

df_selection = df.query("Category in @category & Label in @label")

st.dataframe(df_selection)
