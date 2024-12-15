from zoo.zoo import Zoo
from zoo.visitor import Visitor
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

    visitors = {}

    print("Välkommen till Djurparken!")
    print("1. Visa information om djurparken")
    print("2. Köpa biljett")
    print("3. Logga in som besökare")
    print("4. Avsluta")

    while True:
        choice = input("\nVad vill du göra? (1-4): ")
        if choice == "1":
            print(f"\nParkens öppettider: {my_zoo.show_opening_hours()}")
            print(f"Biljettkostnad: {my_zoo.show_ticket_price()}")
            print("\nTillgängliga tillval och priser:")
            print(my_zoo.show_addon_prices())
            print("\nDjur i parken:")
            for animal in my_zoo.list_animals():
                print(animal)
        elif choice == "2":
            name = input("Ange ditt namn: ")
            budget = float(input("Ange din budget: "))
            visitor = Visitor(name, budget)
            visitors[name] = visitor
            print(f"\nVälkommen {name}! Din budget är {budget} SEK.")
        elif choice == "3":
            name = input("Ange ditt namn: ")
            if name not in visitors:
                print(f"\nIngen besökare med namnet {name} hittades.")
                continue
            visitor = visitors[name]
            visitor_menu(visitor, my_zoo)
        elif choice == "4":
            print("Tack för ditt besök! Välkommen åter!")
            break
        else:
            print("Ogiltigt val, försök igen.")

def visitor_menu(visitor, zoo):
    print(f"\nVälkommen tillbaka, {visitor.name}!")
    print("1. Visa tillgängliga tillval")
    print("2. Lägg till tillval")
    print("3. Utforska djurparken")
    print("4. Gå tillbaka")

    while True:
        choice = input("\nVad vill du göra? (1-4): ")
        if choice == "1":
            print("\nTillgängliga tillval:")
            print(zoo.show_addon_prices())
        elif choice == "2":
            addon = input("Ange tillval: ")
            if addon in zoo.addons:
                price = zoo.addons[addon]
                print(visitor.add_to_cart(addon, price))
            else:
                print(f"{addon} finns inte som tillval.")
        elif choice == "3":
            explore_park(visitor, zoo)
        elif choice == "4":
            print("Går tillbaka till huvudmenyn...")
            break
        else:
            print("Ogiltigt val, försök igen.")

def explore_park(visitor, zoo):
    print(f"\nUtforskar parken för {visitor.name}:")
    if "Detaljerad info" in [item[0] for item in visitor.cart]:
        print("\nDjur i parken:")
        for animal in zoo.list_animals():
            print(animal)
    else:
        print("Du har inte köpt tillgång till detaljerad information.")

    if "Mata djur" in [item[0] for item in visitor.cart]:
        name = input("Ange djurets namn för matning: ")
        food = input("Vad vill du mata djuret med? ")
        print(zoo.feed_animal(name, food))
    else:
        print("Du har inte köpt tillgång till att mata djur.")

if __name__ == "__main__":
    main()
