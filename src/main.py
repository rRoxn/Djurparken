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
    print("1. Visa biljettpris och tillval")
    print("2. Lägg till en besökare")
    print("3. Lista besökare")
    print("4. Köp biljetter och tillval")
    print("5. Avsluta")

    # Loop för val i menyn
    while True:
        choice = input("\nVad vill du göra? (1-5): ")
        if choice == "1":
            print(my_zoo.show_ticket_price())
            print("Tillgängliga tillval:")
            print(my_zoo.show_addon_prices())
        elif choice == "2":
            visitor_name = input("Ange besökarens namn: ")
            budget = float(input("Ange besökarens budget: "))
            visitor = Visitor(visitor_name, budget)
            my_zoo.add_visitor(visitor)
            print(f"Besökaren {visitor_name} har lagts till.")
        elif choice == "3":
            print("\nLista över besökare:")
            print(my_zoo.list_visitors())
        elif choice == "4":
            visitor_name = input("Ange besökarens namn: ")
            visitor = next((v for v in my_zoo.visitors if v.name == visitor_name), None)
            if not visitor:
                print(f"Ingen besökare med namnet {visitor_name} hittades.")
                continue
            print(visitor.view_cart())
            while True:
                addon = input("Ange ett tillval att köpa (eller skriv 'klar' för att avsluta): ")
                if addon.lower() == "klar":
                    break
                if addon in my_zoo.addons:
                    price = my_zoo.addons[addon]
                    print(visitor.add_to_cart(addon, price))
                else:
                    print(f"Tillvalet '{addon}' finns inte.")
            print(visitor.purchase())
        elif choice == "5":
            print("Tack för ditt besök!")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()
