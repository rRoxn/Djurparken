from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int, favorite_food: str, image_path: str):
        """Initierar ett djur."""
        self.name = name
        self.age = age
        self.favorite_food = favorite_food
        self.hungry = False
        self.image_path = image_path

    @abstractmethod
    def interact(self):
        """Interagerar med djuret. Måste implementeras av subklasser."""
        pass

    @abstractmethod
    def eat(self, food: str):
        """Funktion för att mata djuren. Måste implementeras av subklasser."""
        pass
