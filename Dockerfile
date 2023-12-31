FROM debian:stable

RUN apt-get update
RUN apt-get install -y python3-full

WORKDIR /var/chatbot

RUN python3 -m venv ./venv
RUN ./venv/bin/pip3 install openai streamlit

ADD src ./

EXPOSE 8501/tcp
CMD [ "/var/chatbot/venv/bin/streamlit", "run", "./app.py" ]