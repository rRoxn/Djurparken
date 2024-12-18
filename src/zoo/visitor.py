class Visitor:
    def __init__(self, name: str, budget: float):
        """
        Initierar en besökare med budget och kundvagn.

        :param name: Besökarens namn
        :param budget: Tillgänglig budget
        """
        self.name = name
        self.budget = budget
        self.cart = []  # Lista över tillval som tuples (item, price)

    def add_to_cart(self, item: str, price: float) -> bool:
        """
        Lägger till ett tillval i kundvagnen om budgeten räcker.

        :param item: Namnet på tillvalet
        :param price: Priset för tillvalet
        :return: True om tillvalet lades till, annars False
        """
        if self.budget >= price:
            self.cart.append((item, price))
            self.budget -= price
            return True
        return False

    def summarize_cart(self) -> str:
        """Returnerar en sammanställning av kundvagnen."""
        if not self.cart:
            return "Kundvagnen är tom."
        total_cost = sum(item[1] for item in self.cart)
        items = "\n".join(f"{item[0]}: {item[1]:.2f} SEK" for item in self.cart)
        return f"Din kundvagn:\n{items}\nTotalpris: {total_cost:.2f} SEK"

    def purchase(self) -> str:
        """
        Slutför köpet och tömmer kundvagnen.

        :return: Sträng som bekräftar köpet
        """
        if not self.cart:
            return "Kundvagnen är tom, inget att köpa."
        self.cart.clear()
        return "Köpet har slutförts! Tack för ditt besök."

    def __str__(self):
        """Returnerar en strängrepresentation av besökaren."""
        return f"{self.name} - Budget: {self.budget:.2f} SEK"
