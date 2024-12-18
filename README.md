Om Projektet
Djurparken är ett interaktivt program där användare kan utforska en virtuell djurpark. Programmet erbjuder funktioner som att visa djurens detaljer, mata och interagera med djuren, samt hantera tillval för att förbättra besöksupplevelsen.

Projektet är byggt med Python och har ett grafiskt användargränssnitt (GUI) baserat på Tkinter. Koden är strukturerad med objektorienterad programmering (OOP) och inkluderar separata moduler för logik och gränssnitt.

Kom igång
Förberedelser
Klona projektet:

bash
git clone <repository-url>
cd Djurparken
Skapa en virtuell miljö (rekommenderas):

bash
python -m venv env
source env/bin/activate    # macOS/Linux
env\Scripts\activate       # Windows
Installera beroenden:

bash
pip install -r requirements.txt
Starta Programmet
Kör följande kommando för att starta applikationen:

bash
python src/main.py
Använd GUI:t för att navigera mellan olika sidor, utforska djur, mata dem och köpa tillval.

Testning
För att köra automatiserade tester, använd:

bash
pytest
Testerna är designade för att validera funktionaliteten hos klasser och metoder.

Filstruktur
src/: Innehåller källkoden för applikationen.
main.py: Startpunkt för programmet.
zoo/: Hanterar djurparkens logik.
animals/: Klasser för djuren i parken.
gui.py: Grafiskt användargränssnitt.
tests/: Tester för att verifiera funktionaliteten.
docs/: Dokumentation av projektet.
assets/: Bilder och andra resurser.

Licens
Detta projekt är utvecklat för utbildningsändamål och är fritt att använda och modifiera.