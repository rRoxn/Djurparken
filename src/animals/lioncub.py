from animals.lion import Lion

class LionCub(Lion):
    def __init__(self, name: str, months: int):
        """Initierar en lejonunge"""
        super().__init__(name, age=0) #Sätter ålder som 0 för att ärva av lion korrekt
        self.months = months


    def get_info(self):
        """Returnerar information om lejonunge."""
        years = self.months // 12 #Omvandla år till hela år.
        remaining_months = self.months % 12
        return(
        f"Lejonunge: {self.name}, "
        f"Ålder: {years} år och {remaining_months} månader, "
        f"Favoritmat: {self.favorite_food}"
        )
