import streamlit as st

import styling

styling.apply()

with open("assets/info.md", "r", encoding="utf-8") as info_file:
    st.markdown(info_file.read())