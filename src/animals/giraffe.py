from animals.animal import Animal

class Giraffe(Animal):
    def __init__(self, name: str, age: int, image_path):
        """Initierar en giraff."""
        super().__init__(name, age, "blad", image_path)

    def interact(self):
        """Interaktion för giraff."""
        self.hungry = True  # Giraffen blir hungrig efter interaktion
        return f"{self.name} sträcker sig efter blad."

    def get_info(self):
        """Returnerar information om giraffen."""
        return f"Giraff: {self.name}, Ålder: {self.age}, Favoritmat: {self.favorite_food}"