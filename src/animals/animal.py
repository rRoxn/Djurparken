from abc import ABC, abstractmethod
import os

class Animal(ABC):
    def __init__(self, name: str, age: int, favorite_food: str, image_path: str):
        """
        Initierar ett djur med grundläggande attribut.

        :param name: Djurets namn
        :param age: Djurets ålder
        :param favorite_food: Djurets favoritmat
        :param image_path: Sökväg till djurets bild
        """
        self.name = name
        self.age = age
        self.favorite_food = favorite_food
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(base_dir, "../assets/images", image_path)
        self.hungry = True  # Standardvärde: Alla djur börjar som hungriga
    @abstractmethod
    def interact(self) -> str:
        """
        Definierar hur ett djur interagerar. Måste implementeras i subklasser.

        :return: En sträng som beskriver interaktionen
        """
        pass

    @abstractmethod
    def eat(self, food: str) -> str:
        """
        Definierar hur ett djur äter. Måste implementeras i subklasser.

        :param food: Den mat som erbjuds djuret
        :return: En sträng som beskriver resultatet av matningen
        """
        pass

    def toggle_hunger(self):
        """
        Växlar djurets hungerstatus mellan hungrig och mätt.
        """
        self.hungry = not self.hungry

    def is_hungry(self) -> bool:
        """
        Kontrollerar om djuret är hungrigt.

        :return: True om djuret är hungrigt, annars False
        """
        return self.hungry

    def validate_food(self, food: str) -> bool:
        """
        Validerar om given mat är djurets favoritmat.

        :param food: Mat som ska kontrolleras
        :return: True om maten är favoritmat, annars False
        """
        return food.lower() == self.favorite_food.lower()

    def __str__(self) -> str:
        """
        Returnerar en strängrepresentation av djuret.

        :return: Sträng som beskriver djuret med dess attribut
        """
        return (
            f"Art: {self.get_species()}, Namn: {self.name}, "
            f"Ålder: {self.age}, Favoritmat: {self.favorite_food}, "
            f"Hungrig: {'Ja' if self.hungry else 'Nej'}"
        )

    @abstractmethod
    def get_species(self) -> str:
        """
        Returnerar djurets art. Måste implementeras i subklasser.

        :return: En sträng som representerar djurets art
        """
        pass
