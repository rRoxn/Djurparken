class Visitor:
    def __init__(self, name: str, budget: float):
        """Initierar en besökare."""
        self.name = name
        self.budget = budget
        self.cart = []  # Lista över valda tillval

    def add_to_cart(self, item: str, price: float) -> bool:
        """Lägger till ett tillval i kundvagnen om budgeten räcker."""
        if self.budget >= price:
            self.cart.append((item, price))
            self.budget -= price
            return True  # Returnera True om tillvalet lades till
        return False  # Returnera False om budgeten inte räckte

    def summarize_cart(self) -> str:
        """Visar kundvagnen och totalkostnaden."""
        if not self.cart:
            return "Kundvagnen är tom."
        total_cost = sum(item[1] for item in self.cart)
        items = "\n".join(f"{item[0]}: {item[1]} SEK" for item in self.cart)
        return f"Din kundvagn:\n{items}\nTotalpris: {total_cost} SEK"

    def purchase(self) -> str:
        """Slutför köpet och tömmer kundvagnen."""
        if not self.cart:
            return "Kundvagnen är tom, inget att köpa."
        self.cart.clear()
        return "Köpet har slutförts! Tack för ditt besök."

    def __str__(self):
        """Returnerar en strängrepresentation av besökaren."""
        return f"Besökare: {self.name}, Budget: {self.budget} SEK"
