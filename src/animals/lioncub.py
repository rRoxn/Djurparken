from animals.lion import Lion

class LionCub(Lion):
    def __init__(self, name: str, months: int, image_path: str):
        """Initierar en lejonunge"""
        super().__init__(name, age = 0, image_path=image_path) #Sätter ålder som 0 för att ärva av lion korrekt
        self.months = months


    def get_info(self):
        years = self.months // 12
        remaining_months = self.months % 12
        return (
            f"Lejonunge: {self.name}, Ålder: {years} år och {remaining_months} månader, "
            f"Favoritmat: {self.favorite_food}, Bildväg: {self.image_path}"
            )

    def get_age_in_month(self):
        """Retunerar åldern i månader"""
        return self.months


    def eat(self, food: str):
        """Lejonungens specifika sätt att äta."""
        if food == self.favorite_food:
            self.hungry = False
            return f"{self.name} tuggar försiktigt på {food} medan den leker."
        else:
            return f"{self.name} vägrar äta {food} och försöker leka istället."
