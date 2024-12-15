from src.gui import MainApp
from zoo.zoo import Zoo
from animals.lion import Lion
from animals.lioncub import LionCub
from animals.giraffe import Giraffe
from animals.elephant import Elephant


def main():
    # Skapa djurparken
    my_zoo = Zoo(
        name="Eggis Zoo",
        opening_hours="09:00 - 18:00",
        ticket_price=150.0,
        addons={"Mata djur": 50.0, "Interagera med djur": 70.0},
    )

    # Lägg till djur
    my_zoo.add_animal(Lion("Simba", 5, "../assets/images/lion.png"))
    my_zoo.add_animal(LionCub("Nala", 14, "../assets/images/lioncub.jpeg"))
    my_zoo.add_animal(Giraffe("Melman", 7, "../assets/images/giraffe.png"))
    my_zoo.add_animal(Elephant("Dumbo", 24, "../assets/images/elephant.png"))

    # Starta GUI
    app = MainApp(my_zoo)
    app.mainloop()

if __name__ == "__main__":
    main()
