import streamlit as st
import time

import base64

# Function to convert image to base64
def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Base64 encoding
img_base64 = img_to_base64("iphone_home_screen.jpg")

# Setting the page configuration
st.set_page_config(
    page_title="iPhone Home Screen",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Display the iPhone home screen as a background image
st.markdown(
    f"""
    <style>
        div.stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: 400px 800px;
            background-repeat: no-repeat;
            background-position: center;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Custom CSS for the iPhone message popup
st.markdown(
    """
    <style>
        .iphone-popup {
            background-color: #ffffff;
            border-radius: 20px;
            padding: 20px;
            width: 300px;
            position: fixed;
            top: 120px;
            left: 50%;
            transform: translate(-50%, 0);
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 999;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Placeholder for the popup message
popup_placeholder = st.empty()

# Delay for 5 seconds
time.sleep(1)

# Display the popup message
popup_placeholder.markdown(
    """
    <div class="iphone-popup">
        <p>Es scheint als hätte Ihr Arzt ein Röntgenbild hochgeladen. Möchten Sie mehr dazu erfahren?</p>
    </div>
    """,
    unsafe_allow_html=True,
)
