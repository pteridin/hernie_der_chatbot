import streamlit as st
import openai

def hide_streamlit_widgets():
    hide_footer_style = """
    <style>
    div.stDeployButton {visibility: hidden;}
    //button {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    button:has(svg) { visibility: visible;}

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

with open("./primer.md", "r", encoding="utf-8") as primer_file:
    prompt_primer = primer_file.read()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []



# Write intro
with st.chat_message("assistant"):
    st.write("""Hallo Herbert, hier ist Hernie! 👋
             
Ich bin ein digitaler Assistent zu deiner Erkrankung, und unterstütze dich bei deiner Behandlung.
Du kannst Fragen zu deiner Erkrankung stellen und dich dazu beraten lassen, wie deine Erkrankung
behandelt werden soll.

Möchtest du die Informationen kompakt erhalten klicke auf diesen Link.

Möchtest du dich mit einem Kassenmitarbeiter verbinden rufe unter folgender Nummer an: 0211-123455 

Oder stelle einfach eine Frage, wie 'Kann meine Erkrankung auch ambulant behandelt werden?'
""")
    
# handle chat history
for message in st.session_state.messages:
    if(message["role"] != "system"):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


prompt = st.chat_input("Frage etwas")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.session_state.prompt = []
    st.session_state.prompt.append({"role": "system", "content": prompt_primer})
    st.session_state.prompt.append({"role": "user", "content": prompt})
    
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.prompt)
    answer = chat_completion.choices[0].message.content
    with st.chat_message("assistant"):
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    