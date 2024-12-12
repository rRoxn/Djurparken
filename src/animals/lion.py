from animals.animal import Animal

class Lion(Animal):
    #Parameterar
    def __init__(self, name: str, age: int, image_path):
        """Initierar ett lejon."""
        super().__init__(name, age, "kött", image_path)

    def get_info(self):
        """Returnerar information om lejonet."""
        return f"Lejon: {self.name}, Ålder: {self.age}, Favoritmat: {self.favorite_food}"

    def interact(self):
        self.hungry = True
        return f"{self.name} tittar stolt på dig."
