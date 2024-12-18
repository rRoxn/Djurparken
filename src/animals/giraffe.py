from animals.animal import Animal

class Giraffe(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """
        Initierar en giraff med specifika attribut.

        :param name: Giraffens namn
        :param age: Giraffens ålder
        :param image_path: Sökväg till giraffens bild
        """
        super().__init__(name, age, "Blad", image_path)

    def interact(self) -> str:
        """
        Hanterar interaktion med giraffen.

        :return: Beskrivning av interaktionen.
        """
        self.hungry = True  # Giraffen blir hungrig efter interaktion
        return f"{self.name} sträcker sig efter blad."

    def eat(self, food: str) -> str:
        """
        Giraffens specifika sätt att äta.

        :param food: Mat som ges till giraffen.
        :return: Beskrivning av hur giraffen reagerar.
        """
        if not self.is_hungry():
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):
            self.toggle_hunger()
            return f"{self.name} sträcker sin långa hals för att nå {food}."
        return f"{self.name} ignorerar {food} och letar efter blad istället."

    def get_species(self) -> str:
        """
        Returnerar artens namn.

        :return: Sträng som representerar arten.
        """
        return "Giraff"