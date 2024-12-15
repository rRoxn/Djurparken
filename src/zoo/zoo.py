class Zoo:
    def __init__(self, name: str, opening_hours: str, ticket_price: float, addons: dict):
        """Initierar djurparken."""
        self.name = name
        self.opening_hours = opening_hours
        self.ticket_price = ticket_price
        self.addons = addons
        self.animals = []  # Lista över alla djur
        self.visitors = []  # Lista över besökare, max 3

    def add_animal(self, animal):
        """Lägger till ett djur i djurparken."""
        self.animals.append(animal)

    def list_animals(self, detailed=False):
        """Returnerar en lista med förenklad eller detaljerad information om djuren."""
        if detailed:
            return [str(animal) for animal in self.animals]  # Full info med __str__
        else:
            return self.animals  # Returnera djurobjekt

    def show_ticket_price(self) -> str:
        """Returnerar biljettpris."""
        return f"Biljettpris: {self.ticket_price} SEK."

    def show_opening_hours(self) -> str:
        """Returnerar öppettider för djurparken."""
        return f"Öppettider: {self.opening_hours}."

    def show_addon_prices(self) -> str:
        """Visar tillgängliga tillval och deras priser."""
        return "\n".join(f"{addon}: {price} SEK" for addon, price in self.addons.items())

    def feed_animal(self, name: str, food: str) -> str:
        """Matar ett djur i djurparken."""
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal.eat(food)
        return f"Inget djur med namnet '{name}' hittades."

    def add_visitor(self, visitor) -> str:
        """Lägger till en besökare om maxgränsen inte är nådd."""
        if len(self.visitors) < 3:
            self.visitors.append(visitor)
            return f"Besökaren {visitor.name} har lagts till."
        return "Maxgränsen för 3 besökare är nådd."

    def list_visitors(self) -> str:
        """Returnerar en lista över alla registrerade besökare."""
        if not self.visitors:
            return "Inga besökare är registrerade."
        return "\n".join(str(visitor) for visitor in self.visitors)

    def remove_visitor(self, name: str) -> str:
        """Tar bort en specifik besökare från listan."""
        for visitor in self.visitors:
            if visitor.name.lower() == name.lower():
                self.visitors.remove(visitor)
                return f"Besökaren {name} har tagits bort."
        return f"Ingen besökare med namnet {name} hittades."

    def interact_with_animal(self, name, interaction_type):
        for animal in self.animals:
            if animal.name == name:
                return animal.interact()
        return f"Inget djur med {name} hittat."

    def __str__(self):
        """Returnerar en strängrepresentation av djurparken."""
        return (
            f"Djurparken: {self.name}\n"
            f"Öppettider: {self.opening_hours}\n"
            f"Biljettpris: {self.ticket_price} SEK\n"
            f"Antal djur: {len(self.animals)}\n"
            f"Antal besökare: {len(self.visitors)}"
        )