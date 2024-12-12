from animals.animal import Animal

class Lion(Animal):
<<<<<<< HEAD
    #Parameterar
    def __init__(self, name: str, age: int, image_path):
=======
    def __init__(self, name: str, age: int, image_path: str):
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862
        """Initierar ett lejon."""
        super().__init__(name, age, "kött", image_path)


    def interact(self):
        self.hungry = True
        return f"{self.name} tittar stolt på dig."

    def eat(self, food: str):
        """Lejonets specifika sätt att äta."""
        if food == self.favorite_food:
            self.hungry = False
            return f"{self.name} sliter i sig {food} med en kraftig riv!"
        else:
            return f"{self.name} rynkar på nosen och vägrar äta {food}."


    def get_info(self):
        return (
            f"Lejon: {self.name}, Ålder: {self.age}, "
            f"Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}"
            )
