import os
from gui import MainApp
from zoo.zoo import Zoo
from animals.lion import Lion
from animals.lioncub import LionCub
from animals.giraffe import Giraffe
from animals.elephant import Elephant

def main():
    # Basväg för assets/images
    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, "../assets/images")

    # Skapa djurparken
    my_zoo = Zoo(
        name="Eggis Zoo",
        opening_hours="09:00 - 18:00",
        ticket_price=150.0,
        addons={"Mata djur": 50.0, "Interagera med djur": 70.0},
    )

    # Lägg till djur med dynamiska sökvägar
    my_zoo.add_animal(Lion("Simba", 5, os.path.join(images_dir, "lion.png")))
    my_zoo.add_animal(LionCub("Nala", 14, os.path.join(images_dir, "lioncub.jpeg")))
    my_zoo.add_animal(Giraffe("Melman", 7, os.path.join(images_dir, "giraffe.png")))
    my_zoo.add_animal(Elephant("Dumbo", 24, os.path.join(images_dir, "elephant.png")))

    # Starta GUI
    app = MainApp(my_zoo)
    app.mainloop()

if __name__ == "__main__":
    main()