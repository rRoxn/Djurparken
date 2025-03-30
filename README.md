# Djurparken (The Zoo)

Ett interaktivt program för att utforska och hantera en virtuell djurpark, byggt med Python och Tkinter.

## 🌟 Funktioner

- Utforska olika djur i djurparken
- Se detaljerad information om varje djur
- Mata och interagera med djuren
- Köp tillval för en förbättrad upplevelse
- Grafiskt användargränssnitt för enkel navigation

## 📋 Krav

- Python 3.8 eller senare
- pip (Python's pakethanterare)
- Git (för att klona projektet)

## 🚀 Installation

1. **Klona projektet**

   ```bash
   git clone https://github.com/[användarnamn]/Djurparken.git
   cd Djurparken
   ```

2. **Skapa en virtuell miljö**

   På macOS/Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   På Windows:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Installera beroenden**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Användning

1. **Starta programmet**

   ```bash
   python src/main.py
   ```

2. **Navigera i programmet**
   - Använd menyn för att välja olika funktioner
   - Klicka på djuren för att se mer information
   - Använd knapparna för att interagera med djuren
   - Köp tillval via menyn

## 🧪 Testning

Kör testerna med följande kommando:

```bash
pytest
```

## 📁 Projektstruktur

```
Djurparken/
├── src/
│   ├── main.py           # Programmets startpunkt
│   ├── gui.py            # Grafiskt gränssnitt
│   ├── zoo/
│   │   └── zoo.py        # Djurparkens huvudlogik
│   └── animals/          # Djurklasser
│       ├── lion.py
│       ├── lioncub.py
│       ├── giraffe.py
│       └── elephant.py
├── assets/
│   └── images/           # Bilder för djuren
├── tests/                # Testfiler
├── docs/                 # Dokumentation
└── requirements.txt      # Projektberoenden
```

## 🛠️ Utveckling

För att bidra till projektet:

1. Forka repositoryt
2. Skapa en ny branch för din feature
3. Gör dina ändringar
4. Kör testerna för att säkerställa att allt fungerar
5. Skicka en pull request

## 📝 Licens

Detta projekt är utvecklat för utbildningsändamål och är fritt att använda och modifiera.

## ⚠️ Viktigt

- Säkerställ att du har rätt Python-version installerad
- Använd alltid den virtuella miljön när du arbetar med projektet
- Se till att alla tester går igenom innan du gör några ändringar
