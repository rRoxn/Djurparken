from animals.animal import Animal

class Giraffe(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """Initierar en giraff."""
        super().__init__(name, age, "blad", image_path)

    def interact(self) -> str:
        """Interaktion för giraff."""
        self.hungry = True  # Giraffen blir hungrig efter interaktion
        return f"{self.name} sträcker sig efter blad."

    def eat(self, food: str) -> str:
        """Giraffens specifika sätt att äta."""
        if not self.hungry:
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):
            self.hungry = False
            return f"{self.name} sträcker sin långa hals för att nå {food}."
        return f"{self.name} ignorerar {food} och letar efter blad istället."

    def get_species(self) -> str:
        """Returnerar artens namn."""
        return "Giraff"

    def __str__(self) -> str:
        """Returnerar en strängrepresentation av giraffens attribut."""
        return (
            f"Art: {self.get_species()}, Namn: {self.name}, "
            f"Ålder: {self.age}, Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}, "
            f"Hungrig: {'Ja' if self.hungry else 'Nej'}"
            )