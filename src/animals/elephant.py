from animals.animal import Animal

class Elephant(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """Initierar en elefant."""
        super().__init__(name, age, "jordnötter", image_path)

    def interact(self) -> str:
        """Interaktion för elefant."""
        self.hungry = True  # Elefanten blir hungrig efter interaktion
        return f"{self.name} låter dig klappa dess snabel."

    def eat(self, food: str) -> str:
        """Elefantens specifika sätt att äta."""
        if not self.hungry:
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):
            self.hungry = False
            return f"{self.name} plockar upp {food} med snabeln och äter det långsamt."
        return f"{self.name} trumpetar högt och vägrar äta {food}."

    def get_species(self) -> str:
        """Returnerar artens namn."""
        return "Elefant"

    def __str__(self) -> str:
        """Returnerar en strängrepresentation av elefantens attribut."""
        return (
            f"Art: {self.get_species()}, Namn: {self.name}, "
            f"Ålder: {self.age}, Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}, "
            f"Hungrig: {'Ja' if self.hungry else 'Nej'}"
        )
