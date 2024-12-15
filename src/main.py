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
        addons={"Mata djur": 50.0, "Interagera med djur": 70.0},
    )

    # Lägg till djur
    my_zoo.add_animal(Lion("Simba", 5, "assets/images/lion.png"))
    my_zoo.add_animal(LionCub("Nala", 14, "assets/images/lioncub.jpeg"))
    my_zoo.add_animal(Giraffe("Melman", 7, "assets/images/giraffe.png"))
    my_zoo.add_animal(Elephant("Dumbo", 24, "assets/images/elephant.png"))

    while True:
        print("\n--- Startsida ---")
        print("1. Visa enkel information om djurparken")
        print("2. Registrera ny besökare och köp biljett")
        print("3. Visa och hantera besökare")
        print("4. Utforska djurparken")
        print("5. Avsluta")

        choice = input("\nVad vill du göra? (1-5): ")
        if choice == "1":
            show_simple_zoo_info(my_zoo)
        elif choice == "2":
            if len(my_zoo.visitors) < 3:
                register_visitor(my_zoo)
            else:
                print("Maxgränsen för 3 besökare är nådd.")
        elif choice == "3":
            manage_visitors(my_zoo)
        elif choice == "4":
            visit_park(my_zoo)
        elif choice == "5":
            print("Tack för ditt besök! Välkommen åter!")
            break
        else:
            print("Ogiltigt val, försök igen.")

def show_simple_zoo_info(zoo):
    """Visar grundläggande information om djurparken."""
    print(f"\nParkens öppettider: {zoo.show_opening_hours()}")
    print(f"Biljettkostnad: {zoo.show_ticket_price()}")
    print("\nTillgängliga tillval:")
    for i, (addon, price) in enumerate(zoo.addons.items(), start=1):
        print(f"{i}. {addon}: {price} SEK")
    print("\nDjur i parken:")
    for animal in zoo.list_animals():
        print(f"Art: {animal.get_species()}, Namn: {animal.name}")

def register_visitor(zoo):
    """Registrerar en ny besökare och köper biljett."""
    name = input("Ange namn för besökaren: ")
    budget = float(input("Ange budget för besökaren: "))

    if budget < zoo.ticket_price:
        print("\nDu har inte tillräckligt med pengar för att köpa en biljett.")
        return

    budget -= zoo.ticket_price
    visitor = Visitor(name, budget)
    print(zoo.add_visitor(visitor))
    print(f"\nVälkommen {name}! Din återstående budget är {budget} SEK.")

    # Låt besökaren köpa tillval direkt
    purchase_addons(visitor, zoo)

def manage_visitors(zoo):
    """Visa och hantera besökare i djurparken."""
    while True:
        print("\n--- Hantera besökare ---")
        print(zoo.list_visitors())
        print("1. Ta bort en besökare")
        print("2. Gå tillbaka till startsidan")
        choice = input("\nVad vill du göra? (1-2): ")
        if choice == "1":
            name = input("Ange namnet på besökaren att ta bort: ")
            print(zoo.remove_visitor(name))
        elif choice == "2":
            print("Går tillbaka till startsidan...")
            break
        else:
            print("Ogiltigt val, försök igen.")

def visit_park(zoo):
    """Tillåter en registrerad besökare att utforska djurparken."""
    if not zoo.visitors:
        print("\nInga besökare är registrerade ännu.")
        return

    print("\nVälj en besökare att logga in som:")
    for i, visitor in enumerate(zoo.visitors, start=1):
        print(f"{i}. {visitor.name} (Budget: {visitor.budget} SEK)")

    try:
        choice = int(input("\nAnge nummer för besökaren: ")) - 1
        if choice < 0 or choice >= len(zoo.visitors):
            print("Ogiltigt val.")
            return
        visitor = zoo.visitors[choice]
    except ValueError:
        print("Ogiltig inmatning.")
        return

    print(f"\nVälkommen {visitor.name}! Du har tillgång till den detaljerade djurvyn.")
    while True:
        print(f"\n--- Utforska parken: {visitor.name} ---")
        print("1. Visa detaljerad information om djur")
        print("2. Interagera med ett djur (kräver tillval)")
        print("3. Mata ett djur (kräver tillval)")
        print("4. Gå tillbaka till startsidan")

        choice = input("\nVad vill du göra? (1-4): ")
        if choice == "1":
            for animal_info in zoo.list_animals(detailed=True):
                print(animal_info)
        elif choice == "2":
            if "Interagera med djur" in [item[0] for item in visitor.cart]:
                name = input("Ange djurets namn: ")
                for animal in zoo.animals:
                    if animal.name.lower() == name.lower():
                        print(animal.interact())
                        break
                else:
                    print(f"Inget djur med namnet {name} hittades.")
            else:
                print("Du har inte köpt tillvalet för att interagera med djur.")
        elif choice == "3":
            if "Mata djur" in [item[0] for item in visitor.cart]:
                name = input("Ange djurets namn: ")
                food = input("Vad vill du mata djuret med? ")
                print(zoo.feed_animal(name, food))
            else:
                print("Du har inte köpt tillvalet för att mata djur.")
        elif choice == "4":
            print("Går tillbaka till startsidan...")
            break
        else:
            print("Ogiltigt val, försök igen.")

def purchase_addons(visitor, zoo):
    """Tillåter besökaren att köpa tillval."""
    print("\nTillgängliga tillval:")
    addons = list(zoo.addons.items())
    for i, (addon, price) in enumerate(addons, start=1):
        print(f"{i}. {addon}: {price} SEK")

    while True:
        try:
            choice = int(input("Ange nummer för tillval att köpa (eller skriv '0' för att avsluta): "))
            if choice == 0:
                break
            if 1 <= choice <= len(addons):
                addon, price = addons[choice - 1]
                print(visitor.add_to_cart(addon, price))
            else:
                print("Ogiltigt val, försök igen.")
        except ValueError:
            print("Ogiltig inmatning, försök igen.")

if __name__ == "__main__":
    main()
