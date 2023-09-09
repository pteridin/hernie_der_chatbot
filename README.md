# Hernie - Der Chatbot ![🤖](src/assets/icon.png)

Der Chatbot *Hernie* ist eine im Rahmen des [**5. HEALTH INSURANCE HACK&CON**](https://www.health-insurance-hack.de/) entwickelte Idee zur Förderung der Ambulantisierung im Gesundheitswesen. 

Mittels eines Triggers - wie der eAU - soll der Patient unmittelbar an weitere Informationen, Kontakte der Krankenkasse oder aber diesen Chatbot verwiesen werden. Hier wird der Patient über die Erkrankung aufgeklärt und entscheidet selbst, welche Behandlung er für richtig hält.

## Installation ⚙

Das Repository wird mit folgendem Befehl gecloned:

```bash
git clone https://github.com/pteridin/hernie_der_chatbot/
```

Es wird ein API-Key von Open-AI benötigt. Dieser API-Key wird in der Datei `src/app.py` eingesetzt:

```python
openai.api_key = "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"
```

Danach kann auch schon das Docker-Image gebaut werden, bsp. auf Windows mittels PowerShell:

```powershell
Get-Content Dockerfile | docker build --tag=hernie
```

Eine andere Indikation kann mittels Änderungen in der Datei `src/assets/info.md` eingespielt werden.