from animals.animal import Animal

class Giraffe(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """Initierar en giraff."""
        super().__init__(name, age, "Blad", image_path)

    def interact(self) -> str:
        """Interaktion för giraff."""
        self.hungry = True  # Giraffen blir hungrig efter interaktion
        return f"{self.name} sträcker sig efter blad."

    def eat(self, food: str) -> str:
        """Giraffens specifika sätt att äta."""
        if not self.is_hungry():  # Använd basklassens metod
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):  # Kontrollera favoritmat
            self.toggle_hunger()  # Byt hungerstatus
            return f"{self.name} sträcker sin långa hals för att nå {food}."
        return f"{self.name} ignorerar {food} och letar efter blad istället."

    def get_species(self) -> str:
        """Returnerar artens namn."""
        return "Giraff"

