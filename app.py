import streamlit as st

st.title("Covid Vaccine Locator")

with st.form("Vaccine Locations"):
    selection = st.selectbox("Choose", ["A", "B"])
    st.form_submit_button("Submit")

st.write(selection)
