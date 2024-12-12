from animals.animal import Animal

class Elephant(Animal):
<<<<<<< HEAD
    def __init__(self, name: str, age: int, image_path):
=======
    def __init__(self, name: str, age: int, image_path: str):
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862
        super().__init__(name, age, "jordnötter", image_path)

    def get_info(self):
        return (
            f"Elefant: {self.name}, Ålder: {self.age}, "
            f"Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}"
            )

    def interact(self):
        self.hungry = True
        return f"{self.name} låter dig klappa dess snabel."

    def eat(self, food: str):
        """Elefantens specifika sätt att äta."""
        if food == self.favorite_food:
            self.hungry = False
            return f"{self.name} plockar upp {food} med snabeln och äter det långsamt."
        else:
            return f"{self.name} trumpetar högt och vägrar äta {food}."
