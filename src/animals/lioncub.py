from animals.lion import Lion

class LionCub(Lion):
    def __init__(self, name: str, months: int, image_path: str):
        """
        Initierar en lejonunge med specifika attribut.

        :param name: Lejonungens namn
        :param months: Lejonungens ålder i månader
        :param image_path: Sökväg till lejonungens bild
        """
        super().__init__(name, age=0, image_path=image_path)  # Ålder sätts till 0 eftersom månader används
        self.months = months

    def eat(self, food: str) -> str:
        """
        Lejonungens specifika sätt att äta.

        :param food: Mat som ges till lejonungen.
        :return: Beskrivning av hur lejonungen reagerar.
        """
        if not self.is_hungry():
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):
            self.toggle_hunger()
            return f"{self.name} tuggar försiktigt på {food} medan den leker."
        return f"{self.name} vägrar äta {food} och försöker leka istället."

    def get_age_in_month(self) -> int:
        """
        Returnerar lejonungens ålder i månader.

        :return: Ålder i månader.
        """
        return self.months

    def interact(self) -> str:
        """
        Hanterar interaktion med lejonungen.

        :return: Beskrivning av interaktionen.
        """
        self.hungry = True
        return f"{self.name} nafsar på ditt finger."

    def get_species(self) -> str:
        """
        Returnerar artens namn.

        :return: Sträng som representerar arten.
        """
        return "Lejon"