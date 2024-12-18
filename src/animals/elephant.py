from animals.animal import Animal


class Elephant(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """
        Initierar en elefant med standardvärden.

        :param name: Elefantens namn
        :param age: Elefantens ålder
        :param image_path: Sökväg till elefantens bild
        """
        super().__init__(name, age, "Jordnötter", image_path)

    def interact(self) -> str:
        """
        Hanterar interaktion med elefanten.

        Elefanten blir hungrig efter interaktionen.
        :return: Beskrivning av interaktionen.
        """
        self.hungry = True  # Uppdaterar hungerstatus
        return f"{self.name} låter dig klappa dess snabel."

    def eat(self, food: str) -> str:
        """
        Elefantens specifika sätt att äta.

        :param food: Mat som ges till elefanten.
        :return: Beskrivning av hur elefanten reagerar.
        """
        if not self.is_hungry():  # Kontrollera om elefanten är hungrig
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):  # Kontrollera om maten är elefantens favoritmat
            self.toggle_hunger()  # Ändra hungerstatus
            return f"{self.name} plockar upp {food} med snabeln och äter det långsamt."
        return f"{self.name} trumpetar högt och vägrar äta {food}."

    def get_species(self) -> str:
        """
        Returnerar artens namn.

        :return: Sträng som representerar arten.
        """
        return "Elefant"
