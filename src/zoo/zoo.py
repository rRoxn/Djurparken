class Zoo:
    def __init__(self, name: str, opening_hours: str, ticket_price: float, addons: dict):
        """Initierar djurparken."""
        self.name = name
        self.opening_hours = opening_hours
        self.ticket_price = ticket_price
        self.addons = addons
        self.animals = []  # Lista över alla djur

    def add_animal(self, animal):
        """Lägger till ett djur i djurparken."""
        self.animals.append(animal)

    def list_animals(self):
        """Returnerar en lista med information om alla djur."""
        return [animal.get_info() for animal in self.animals]

    def search_animal(self, name: str):
        """Söker efter ett djur baserat på dess namn."""
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal.get_info()
        return f"Inget djur med namnet {name} hittades."