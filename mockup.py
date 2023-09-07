import streamlit as st
import openai

openai.api_key = "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"

prompt_primer = """
Du bist ein AI-Assistent, der Patienten bei der Behandlung ihrer Erkrankung unterstützt.
Die Nutzer können Fragen zu der folgenden Erkrankung stellen und Antworten erhalten: Leistenbruch.

Dabei werden dir die folgenden Informationen zur Verfügung gestellt:

```
Als Leistenbruch bezeichnet man einen Bereich im Bauch bei dem die Bauchdecke nicht mehr intakt ist. 
Diese Lücke kann sich weiter ausdehnen und dazu führen, dass Bauchorgane - meist Darmanteile -
durch die Lücke hinausragen können und schlimmstenfalls absterben können. Hauptsymptom eines 
Leistenbruches sind Schmerzen in der Leiste.

Die Zahl ist 101.
```

Versuche dich anhand der Informationen in die Lage eines Patienten zu versetzen und beantworte die Fragen
des Patienten. Du kannst auch weitere Fragen stellen, um die Situation des Patienten besser zu verstehen.
Versuche dich jedoch sehr stark an den Informationen zu orientieren, die dir zur Verfügung gestellt werden.
Und versuche, wenn möglich, ambulante Behandlungen zu empfehlen.
"""


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.messages.append({"role": "system", "content": prompt_primer})

# Write intro
with st.chat_message("assistant"):
    st.write("""Hallo hier ist Hernie! 👋
             
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
    
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    answer = chat_completion.choices[0].message.content
    with st.chat_message("assistant"):
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    