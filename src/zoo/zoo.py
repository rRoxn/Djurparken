class Zoo:
    def __init__(self, name: str, opening_hours: str, ticket_price: float, addons: dict):
        """Initierar djurparken."""
        self.name = name
        self.opening_hours = opening_hours
        self.ticket_price = ticket_price
        self.addons = addons
        self.animals = []  # Lista över alla djur
        self.selected_addons = []  # Lista över valda tillval
        self.visitors = []  # Lista över besökare

    def add_animal(self, animal):
        """Lägger till ett djur i djurparken."""
        self.animals.append(animal)

    def show_ticket_price(self) -> str:
        """Returnerar biljettpris."""
        return f"Biljettpris: {self.ticket_price} SEK."

    def show_opening_hours(self) -> str:
        """Returnerar öppettider för djurparken."""
        return f"Öppettider: {self.opening_hours}."

    def show_addon_prices(self) -> str:
        """Visar tillgängliga tillval och deras priser."""
        return "\n".join(f"{addon}: {price} SEK" for addon, price in self.addons.items())

    def add_to_cart(self, addon: str) -> str:
        """Lägger till ett tillval i kundvagnen om det existerar."""
        if addon in self.addons:
            self.selected_addons.append(addon)
            return f"Tillvalet '{addon}' har lagts till i kundvagnen."
        return f"Tillvalet '{addon}' är inte tillgängligt."

    def summarize_cart(self) -> str:
        """Summerar valda tillval i kundvagnen."""
        if not self.selected_addons:
            return "Kundvagnen är tom."
        total_price = sum(self.addons[addon] for addon in self.selected_addons)
        summary = "\n".join(self.selected_addons)
        return f"Valda tillval:\n{summary}\nTotalpris: {total_price} SEK."

    def purchase(self) -> str:
        """Slutför köpet av valda tillval."""
        if not self.selected_addons:
            return "Kundvagnen är tom. Inget att köpa."
        self.selected_addons.clear()
        return "Köpet har slutförts. Tack för ditt besök!"

    def add_visitor(self, visitor) -> None:
        """Lägger till en besökare till djurparken."""
        self.visitors.append(visitor)

    def list_visitors(self) -> str:
        """Returnerar en lista med alla besökare."""
        if not self.visitors:
            return "Inga besökare i djurparken."
        return "\n".join(visitor.name for visitor in self.visitors)

    def __str__(self):
        """Returnerar en strängrepresentation av djurparken."""
        return (
            f"Djurparken: {self.name}\n"
            f"Öppettider: {self.opening_hours}\n"
            f"Biljettpris: {self.ticket_price} SEK\n"
            f"Antal djur: {len(self.animals)}"
        )
