from animals.lion import Lion

class LionCub(Lion):
    def __init__(self, name: str, months: int, image_path: str):
        """Initierar en lejonunge."""
        super().__init__(name, age=0, image_path=image_path)  # Ålder sätts till 0 eftersom månader används
        self.months = months

    def eat(self, food: str) -> str:
        """Lejonungens specifika sätt att äta."""
        if not self.is_hungry():  # Använd basklassens metod
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):  # Kontrollera favoritmat
            self.toggle_hunger()  # Byt hungerstatus
            return f"{self.name} tuggar försiktigt på {food} medan den leker."
        return f"{self.name} vägrar äta {food} och försöker leka istället."

    def get_age_in_month(self) -> int:
        """Returnerar åldern i månader."""
        return self.months


    def interact(self) -> str:
        """Interaktion för lejonungen."""
        self.hungry = True
        return f"{self.name} nafsar på ditt finger."

    def get_species(self) -> str:
        """Returnerar artens namn."""
        return "Lejon"

