from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int, favorite_food: str):
        """Initierar ett djur."""
        self.name = name
        self.age = age
        self.favorite_food = favorite_food
        self.hungry = False

    @abstractmethod
    def get_info(self):
        """Returnerar information om djuret."""
        pass

    def feed(self, food: str):
        """Matar djuret och uppdaterar hungerstatus."""
        if food == self.favorite_food:
            self.hungry = False
            return f"{self.name} åt upp {food}!"
        return f"{self.name} vill inte äta {food}."

    
