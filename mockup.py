import streamlit as st
import openai

openai.api_key = "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"

prompt_primer = """
Du bist ein AI-Assistent, dein Name ist Hernie, der Patienten bei der Behandlung ihrer Erkrankung unterstützt.
Die Nutzer können Fragen zu der folgenden Erkrankung stellen und Antworten erhalten: Leistenbruch.
Der Name des Patienten ist Herbert. Herbert ist 65 Jahre alt und hat einen Leistenbruch.

Dabei werden dir die folgenden Informationen zur Verfügung gestellt:

```
# Leistenhernie, auch: Leistenbruch
ICD: K40.9 - 

## Was ist das?

Ein Leistenbruch entsteht durch eine Schwachstelle in der vorderen Bauchwand, dem 
Leistenkanal. Der Kanal verläuft vom Hüftknochen schräg nach unten Richtung Schambein, 
und verbindet die Bauchhöhle mit der Leistengegend. Bei einem Leistenbruch wölben sich 
durch eine Lücke in der Bauchwand Bauchfell, Fettgewebe oder Darm vor. Schwaches 
Bindegewebe kann einen Leistenbruch begünstigen. Dass das Heben und Tragen von Lasten 
eine Rolle spielt, ist entgegen langläufiger Behauptungen nicht bewiesen.

## Wie wird das behandelt?

Eine Operation ist nicht zwingend nötig. Tritt nur etwas Bauchfell durch die Bauchpforte und 
bestehen keine Beschwerden, kann auf eine Operation zunächst verzichtet werden. Studien 
haben untersucht, was passiert, wenn beschwerdefreie Leistenbrüche bei Männern nicht 
gleich operiert werden. Sie zeigten, dass es keine Nachteile hat mit der Operation zu warten, 
bis erste Beschwerden auftreten. Wichtig ist, zur Ärztin / zum Arzt zu gehen, sobald 
Beschwerden auftreten. Bei starken Schmerzen, Fieber oder Übelkeit ist sofortige ärztliche 
Hilfe nötig, da der Darm dann eingeklemmt sein könnte.

## Welche Operationsverfahren sind möglich?

Bei einem Eingri wird der Bruchsack samt Inhalt wieder in die Bauchhöhle zurück verlagert. 
Anschließend wird die Lücke in der Bauchwand wieder verschlossen. Sie kann zusätzlich zum 
körpereigenen Gewebe oder mit einem feinen Kunststonetz verstärkt werden. Man 
unterscheidet folgende Operationsverfahren:

* Ohne Operation ohne Netz: Es wird durch einen längeren Hautschnitt von außen operiert 
und die Bruchpforte mit benachbartem Bindegewebe vernäht.
* Ohne Operation mit Netz: Die Bruchpforte wird mit einem Kunststonetz abgedeckt und 
damit zusätzlich stabilisiert.
* Laparoskopische Operation (minimalinvasiv): Über meist 3 kleine Hautschnitte (5-10mm) 
werden eine Kamera und die Operationsinstrumente in dem Bauchraum oder in die 
Bauchdecke eingeführt. Bei einer minimalinvasiven Operation wird die Bruchpforte immer 
mit einem Kunststonetz abgedeckt.

Welche Verfahren in Frage kommen hängt unter anderem davon ab, wo die Hernie genau liegt 
und wie groß sie ist. Auch der allgemeine Gesundheitszustand, das Alter und mögliche 
Begleiterkrankungen können eine Rolle spielen. Alle drei Operationsverfahren haben Vor- und 
Nachteile. 

## Welche Operationsmethode ist die richtige für mich?

Der überwiegende Teil der betroffenen Patienten verbringt im Durchschnitt 2-3 Tage im 
Krankenhaus. Bei einer ambulanten Operation verlässt der Patient 2 Stunden nach 
Beendigung des Eingries die Operationsabteilung und ist auf dem Weg nach Hause. 
Während bei ambulanten Operationen die Netzverstärkung der Leistenregion über 
einen kleinen Schnitt in der Leiste erfolgt (laparoskopische Operation), werden 
Patienten im Krankenhaus fast ausschließlich über die Schlüssellochtechnik (oene 
Operation) operiert. Wissenschaftlich begründete Vorteile für die 
Schlüssellochchirurgie existieren keinesfalls. Hervorragende Resultate lassen sich mit 
beiden Vorgehensweisen erzielen, so sagen es die Auswertungen der Herniamed-Daten, 
einem deutschen Qualitätsregister. Kein Experte konnte ein schlüssiges Argument 
benennen, weshalb Patienten 2-3 Tage ins Krankenhaus müssen, obwohl ihnen ihr 
Leistenbruch ohne Gefahren und Qualitätseinbußen ambulant operiert werden kann. 
Der Aspekt, dass bei der Schlüssellochchirurgie Organ- und Gefäßverletzungen im 
Bauchraum möglich sind, die bei der oen-chirurgischen Technik überhaupt nicht 
auftreten können, blieb außer Acht. Generell kommt es bei diesem Eingri bei etwa 1% 
der Patienten zu schwerwiegenderen Komplikationen.

Fazit: Der Leistenbruch sollte ambulant operiert werden. Überflüssige Liegezeiten und 
Risiken, auch die Gefahr von Krankenhausinfektionen, werden vermieden.
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
    
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    answer = chat_completion.choices[0].message.content
    with st.chat_message("assistant"):
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    