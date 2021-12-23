import streamlit as st

st.title("Covid Vaccine Locator")

with st.form("Vaccine Locations"):
    hospital = st.text_input("Fill in name of hospital")
    st.form_submit_button("Submit")

st.write(hospital)
