class Zoo:
    def __init__(self, name: str, opening_hours: str, ticket_price: float, addons: dict):
        """
        Initierar en instans av djurparken.

        :param name: Namnet på djurparken
        :param opening_hours: Öppettider som sträng
        :param ticket_price: Biljettpris i SEK
        :param addons: Dictionary med tillval och deras priser
        """
        self.__name = name
        self.__opening_hours = opening_hours
        self.__ticket_price = ticket_price
        self._addons = addons
        self.__animals = []  # Privat lista över alla djur
        self._visitors = []  # Skyddad lista över besökare, max 3

    def add_animal(self, animal):
        """Lägger till ett djur i djurparken."""
        self.__animals.append(animal)

    def list_animals(self, detailed=False):
        """
        Returnerar en lista med djur i djurparken.

        :param detailed: Om True, returnera detaljerad information
        :return: Lista över djur som objekt eller strängar
        """
        return [str(animal) for animal in self.__animals] if detailed else self.__animals.copy()

    def show_ticket_price(self) -> str:
        """Returnerar biljettpriset."""
        return f"Biljettpris: {self.__ticket_price} SEK."

    def show_opening_hours(self) -> str:
        """Returnerar öppettider."""
        return f"Öppettider: {self.__opening_hours}."

    def show_addon_prices(self) -> str:
        """Returnerar tillval och deras priser."""
        return "\n".join(f"{addon}: {price} SEK" for addon, price in self._addons.items())

    def feed_animal(self, name: str, food: str) -> str:
        """
        Matar ett specifikt djur.

        :param name: Namnet på djuret
        :param food: Maten som ges
        :return: Sträng med resultatet av matningen
        """
        for animal in self.__animals:
            if animal.name.lower() == name.lower():
                return animal.eat(food)
        return f"Inget djur med namnet '{name}' hittades."

    def add_visitor(self, visitor) -> str:
        """
        Lägger till en besökare i djurparken.

        :param visitor: Besökarobjekt
        :return: Sträng med resultatet
        """
        if len(self._visitors) < 3:
            self._visitors.append(visitor)
            return f"Besökaren {visitor.name} har lagts till."
        return "Maxgränsen för 3 besökare är nådd."

    def list_visitors(self) -> list:
        """Returnerar en lista över alla besökare som strängar."""
        return [str(visitor) for visitor in self._visitors] if self._visitors else []

    def remove_visitor(self, name: str) -> str:
        """
        Tar bort en besökare från parken.

        :param name: Namnet på besökaren
        :return: Sträng med resultatet
        """
        for visitor in self._visitors:
            if visitor.name.lower() == name.lower():
                self._visitors.remove(visitor)
                return f"Besökaren {name} har tagits bort."
        return f"Ingen besökare med namnet {name} hittades."

    def interact_with_animal(self, name: str) -> str:
        """
        Interagerar med ett specifikt djur.

        :param name: Namnet på djuret
        :return: Sträng med resultatet av interaktionen
        """
        for animal in self.__animals:
            if animal.name.lower() == name.lower():
                return animal.interact()
        return f"Inget djur med namnet '{name}' hittades."

    def __str__(self):
        """Returnerar en strängrepresentation av djurparken."""
        return (
            f"Djurparken: {self.__name}\n"
            f"Öppettider: {self.__opening_hours}\n"
            f"Biljettpris: {self.__ticket_price} SEK\n"
            f"Antal djur: {len(self.__animals)}\n"
            f"Antal besökare: {len(self._visitors)}"
        )
