from animals.animal import Animal

class Lion(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """
        Initierar ett lejon med specifika attribut.

        :param name: Lejonets namn
        :param age: Lejonets ålder
        :param image_path: Sökväg till lejonets bild
        """
        super().__init__(name, age, "Kött", image_path)

    def interact(self) -> str:
        """
        Hanterar interaktion med lejonet.

        :return: Beskrivning av interaktionen.
        """
        self.hungry = True
        return f"{self.name} tittar stolt på dig."

    def eat(self, food: str) -> str:
        """
        Lejonets specifika sätt att äta.

        :param food: Mat som ges till lejonet.
        :return: Beskrivning av hur lejonet reagerar.
        """
        if not self.is_hungry():
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):
            self.toggle_hunger()
            return f"{self.name} sliter i sig {food} med en kraftig riv!"
        return f"{self.name} rynkar på nosen och vägrar äta {food}."

    def get_species(self) -> str:
        """
        Returnerar artens namn.

        :return: Sträng som representerar arten.
        """
        return "Lejon"