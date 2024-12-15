from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int, favorite_food: str, image_path: str):
        """Initierar ett djur."""

        self.name = name
        self.age = age
        self.favorite_food = favorite_food
        self.hungry = True
        self.image_path = image_path

    @abstractmethod
    def interact(self) -> str:
        """Interagerar med djuret. Måste implementeras av subklasser."""
        pass

    @abstractmethod
    def eat(self, food: str) -> str:
        """Funktion för att mata djuren. Måste implementeras av subklasser."""
        pass


    def toggle_hunger(self):
        """Byter hungerstatus på djuret."""
        self.hungry = not self.hungry

    def is_hungry(self) -> bool:
        """Kontrollerar om djuret är hungrigt."""
        return self.hungry

    def validate_food(self, food: str) -> bool:
        """Validerar om given mat är djurets favoritmat."""
        return food.lower() == self.favorite_food.lower()


    def __str__(self):
        """Returnerar en strängrepresentation av djuret."""
        return (
            f"Art: {self.get_species()}, Namn: {self.name}, "
            f"Ålder: {self.age}, Favoritmat: {self.favorite_food}, "
            f"Hungrig: {'Ja' if self.hungry else 'Nej'}"
        )
