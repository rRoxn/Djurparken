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
        if not self.is_hungry():  # Använd basklassens metod
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):  # Kontrollera favoritmat
            self.toggle_hunger()  # Byt hungerstatus
            return f"{self.name} plockar upp {food} med snabeln och äter det långsamt."
        return f"{self.name} trumpetar högt och vägrar äta {food}."

    def get_species(self) -> str:
        """Returnerar artens namn."""
        return "Elefant"

