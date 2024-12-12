from animals.animal import Animal

class Elephant(Animal):
    def __init__(self, name: str, age: int, image_path):
        super().__init__(name, age, "jordnötter", image_path)

    def get_info(self):
        return f"Elefant: {self.name}, Ålder: {self.age}, Favoritmat: {self.favorite_food}"

    def interact(self):
        self.hungry = True
        return f"{self.name} låter dig klappa dess snabel."
