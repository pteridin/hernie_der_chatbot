import streamlit as st

with open("assets/info.md", "r", encoding="utf-8") as info_file:
    st.markdown(info_file.read())