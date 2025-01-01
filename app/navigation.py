import streamlit as st

st.set_page_config(page_title="Hassle Medi Bot", page_icon="🧊", layout="centered")

st.navigation({
    "Home": [
        st.Page("pages/main.py", title="Hassle Medi Bot"),
    ],
    "About": [
        st.Page("pages/about.py", title="About"),
    ],
}).run()