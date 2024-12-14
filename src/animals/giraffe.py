from animals.animal import Animal

class Giraffe(Animal):
    def __init__(self, name: str, age: int, image_path: str):
        """Initierar en giraff."""
        super().__init__(name, age, "blad", image_path)


    def get_info(self):
        return (
            f"Giraff: {self.name}, Ålder: {self.age}, "
            f"Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}"
            )

    def interact(self):
        """Interaktion för giraff."""
        self.hungry = True  # Giraffen blir hungrig efter interaktion
        return f"{self.name} sträcker sig efter blad."


    def eat(self, food: str):
        """Giraffens specifika sätt att äta."""
        if food == self.favorite_food:
            self.hungry = False
            return f"{self.name} sträcker sin långa hals för att nå {food}."
        else:
            return f"{self.name} ignorerar {food} och letar efter blad istället."
