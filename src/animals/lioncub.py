from animals.lion import Lion

class LionCub(Lion):
    def __init__(self, name: str, months: int, image_path: str):
        """Initierar en lejonunge."""
        super().__init__(name, age=0, image_path=image_path)  # Ålder sätts till 0 eftersom månader används
        self.months = months

    def get_info(self) -> str:
        """Ger information om lejonungen."""
        years = self.months // 12
        remaining_months = self.months % 12
        return (
            f"Lejonunge: {self.name}, Ålder: {years} år och {remaining_months} månader, "
            f"Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}"
        )

    def eat(self, food: str) -> str:
        """Lejonungens specifika sätt att äta."""
        if not self.hungry:
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):
            self.hungry = False
            return f"{self.name} tuggar försiktigt på {food} medan den leker."
        return f"{self.name} vägrar äta {food} och försöker leka istället."

    def get_age_in_month(self) -> int:
        """Returnerar åldern i månader."""
        return self.months

    def get_species(self) -> str:
        """Returnerar artens namn."""
        return "Lejon"

    def interact(self) -> str:
        """Interaktion för lejonungen."""
        self.hungry = True
        return f"{self.name} nafsar på ditt finger."

    def __str__(self) -> str:
        """Returnerar en strängrepresentation av lejonungens attribut."""
        years = self.months // 12
        remaining_months = self.months % 12
        return (
            f"Art: {self.get_species()}, Namn: {self.name}, "
            f"Ålder: {years} år och {remaining_months} månader, Favoritmat: {self.favorite_food}, "
            f"Bildväg: {self.image_path}, Hungrig: {'Ja' if self.hungry else 'Nej'}"
        )