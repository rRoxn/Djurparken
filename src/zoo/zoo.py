class Zoo:
    def __init__(self, name: str, opening_hours: str, ticket_price: float, addons: dict):
        """Initierar djurparken."""
        #Sätter alla dessa variabler till __private för jag vill ej ändra dessa eller råka gör detta.
        self.__name = name
        self.__opening_hours = opening_hours
        self.__ticket_price = ticket_price
        self._addons = addons
        self.__animals = []  # Lista över alla djur privat
        self._visitors = []  # Lista över besökare, max 3 privat

    def add_animal(self, animal):
        """Lägger till ett djur i djurparken."""
        self.__animals.append(animal)

    def list_animals(self, detailed=False):
        """Returnerar en lista med förenklad eller detaljerad information om djuren."""
        if detailed:
            return [str(animal) for animal in self.__animals]  # Full info med __str__
        else:
            return self.__animals.copy() # Returnera djurobjekt

    def show_ticket_price(self) -> str:
        """Returnerar biljettpris."""
        return f"Biljettpris: {self.__ticket_price} SEK."

    def show_opening_hours(self) -> str:
        """Returnerar öppettider för djurparken."""
        return f"Öppettider: {self.__opening_hours}."

    def show_addon_prices(self) -> str:
        """Visar tillgängliga tillval och deras priser."""
        return "\n".join(f"{addon}: {price} SEK" for addon, price in self._addons.items())

    def feed_animal(self, name: str, food: str) -> str:
        """Matar ett djur i djurparken."""
        for animal in self.__animals:
            if animal.name.lower() == name.lower():
                return animal.eat(food)
        return f"Inget djur med namnet '{name}' hittades."

    def add_visitor(self, visitor) -> str:
        """Lägger till en besökare om maxgränsen inte är nådd."""
        if len(self._visitors) < 3:
            self._visitors.append(visitor)
            return f"Besökaren {visitor.name} har lagts till."
        return "Maxgränsen för 3 besökare är nådd."

    def list_visitors(self) -> list:
        """Returnerar en lista över besökare som strängar."""
        return [str(visitor) for visitor in self._visitors] if self._visitors else []

    def remove_visitor(self, name: str) -> str:
        """Tar bort en specifik besökare från listan."""
        for visitor in self._visitors:
            if visitor.name.lower() == name.lower():
                self._visitors.remove(visitor)
                return f"Besökaren {name} har tagits bort."
        return f"Ingen besökare med namnet {name} hittades."

    def interact_with_animal(self, name):
        for animal in self.__animals:
            if animal.name == name:
                return animal.interact()
        return f"Inget djur med {name} hittat."

    def __str__(self):
        """Returnerar en strängrepresentation av djurparken."""
        return (
            f"Djurparken: {self._visitors}\n"
            f"Öppettider: {self.__opening_hours}\n"
            f"Biljettpris: {self.__ticket_price} SEK\n"
            f"Antal djur: {len(self.__animals)}\n"
            f"Antal besökare: {len(self._visitors)}"
        )