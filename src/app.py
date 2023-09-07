import openai

import streamlit as st
import styling
from io import BytesIO

styling.apply()

def hide_streamlit_widgets():
    hide_footer_style = """
    <style>
    @media (max-width: 800px) {
        .stChatFloatingInputContainer{
            padding-bottom: 24px;
        }
    }
    </style>
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)

hide_streamlit_widgets()

openai.api_key = "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"

with open("assets/primer.md", "r", encoding="utf-8") as primer_file:
    prompt_primer = primer_file.read()

with open("assets/info.md","r", encoding="utf-8") as info_file:
    prompt_primer.replace("###INFO###", info_file.read())

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": """Hallo Herbert, hier ist Hernie! 👋
             
Ich bin ein digitaler Assistent zu deiner Erkrankung, und unterstütze dich bei deiner Behandlung.
Du kannst Fragen zu deiner Erkrankung stellen und dich dazu beraten lassen, wie deine Erkrankung
behandelt werden soll.

Möchtest du die Informationen kompakt erhalten klicke auf diesen [Link](./info).

Möchtest du dich mit einem Kassenmitarbeiter verbinden rufe unter folgender Nummer an: [0211-123455](tel:+49211123455) 

Oder stelle einfach eine Frage, wie 'Kann meine Erkrankung auch ambulant behandelt werden?'
"""    }]
    
# handle chat history
with open("assets/icon.png", "rb") as assistant:
    avatars = {
        "assistant": BytesIO(assistant.read()),
        "user": None
    }
    for message in st.session_state.messages:
        if(message["role"] != "system"):
            with st.chat_message(message["role"], avatar=avatars[message["role"]]):
                st.markdown(message["content"])


prompt = st.chat_input("Frage etwas")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": prompt_primer},
        {"role": "user", "content": prompt}
    ])
    answer = chat_completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})
    
    st.experimental_rerun()