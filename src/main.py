
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
        addons={"Mata djur": 50.0, "Detaljerad info": 30.0},
    )

    # Lägg till djur

    simba = Lion("Simba", 5, "assets/images/lion.png")
    nala = LionCub("Nala", 14, "assets/images/lioncub.jpeg")
    melman = Giraffe("Melman", 7, "assets/images/giraffe.png")
    dumbo = Elephant("Dumbo", 24, "assets/images/elephant.png")

    my_zoo.add_animal(simba)
    my_zoo.add_animal(nala)
    my_zoo.add_animal(melman)
    my_zoo.add_animal(dumbo)

    # Meny för interaktion med djurparken
    print("Välkommen till Djurparken!")
    print("1. Lista alla djur")
    print("2. Sök efter ett djur")
    print("3. Mata ett djur")
    print("4. Avsluta")
    #Loop för val i menyn
    while True:
        choice = input("\nVad vill du göra? (1-4): ")
        if choice == "1":
            print("\nHär är en lista över våra djur:")
            for info in my_zoo.list_animals():
                print(info)
        elif choice == "2":
            name = input("Ange djurets namn: ")
            print(my_zoo.search_animal(name))
        elif choice == "3":
            name = input("Ange djurets namn: ")
            food = input("Vad vill du mata djuret med? ")
            for animal in my_zoo.animals:
                if animal.name.lower() == name.lower():
                    print(animal.feed(food))
                    break
            else:
                print(f"Inget djur med namnet {name} hittades.")
        elif choice == "4":
            print("Tack för ditt besök!")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()
