from animals.animal import Animal

class Lion(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """Initierar ett lejon."""
        super().__init__(name, age, "kött", image_path)

    def interact(self) -> str:
        """Interaktion för lejon."""
        self.hungry = True  # Interaktion gör lejonet hungrigt
        return f"{self.name} tittar stolt på dig."

    def eat(self, food: str) -> str:
        """Lejonets specifika sätt att äta."""
        if not self.hungry:
            return f"{self.name} är inte hungrig."
        if self.validate_food(food):
            self.hungry = False
            return f"{self.name} sliter i sig {food} med en kraftig riv!"
        return f"{self.name} rynkar på nosen och vägrar äta {food}."

    def get_species(self) -> str:
        """Returnerar artens namn."""
        return "Lejon"

    def __str__(self) -> str:
        """Returnerar en strängrepresentation av lejonets attribut."""
        return (
            f"Art: {self.get_species()}, Namn: {self.name}, "
            f"Ålder: {self.age}, Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}, "
            f"Hungrig: {'Ja' if self.hungry else 'Nej'}"
        )
