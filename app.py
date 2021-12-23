import streamlit as st
import pandas as pd

df = pd.read_csv("data/hospitals.csv")

if st.checkbox("Click to show data"):
    st.dataframe(df)

st.title("Covid Vaccine Locator")

with st.form("Vaccine Locations"):
    hospital = st.text_input("Fill in name of hospital")
    st.form_submit_button("Submit")

st.table(df[df["Name"] == hospital])
