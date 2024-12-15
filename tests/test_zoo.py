import pytest
from zoo.zoo import Zoo
from animals.lion import Lion
from animals.elephant import Elephant
from animals.lioncub import LionCub
from animals.giraffe import Giraffe

@pytest.fixture
def example_zoo():
    """Skapar ett exempel-zoo för tester."""
    zoo = Zoo(
        name="Test Zoo",
        opening_hours="10:00 - 16:00",
        ticket_price=100.0,
        addons={
            "Mata djur": 50,
            "Detaljerad information": 30
        }
    )
    zoo.add_animal(Lion("Simba", 5, "assets/images/lion.png"))
    zoo.add_animal(LionCub("Nala", 14, "assets/images/lioncub.png"))
    zoo.add_animal(Giraffe("Melman", 7, "assets/images/giraffe.png"))
    zoo.add_animal(Elephant("Dumbo", 10, "assets/images/elephant.png"))
    return zoo

def test_list_animals(example_zoo):
    result = example_zoo.list_animals()
    assert len(result) == 4
    assert any("Simba" in info for info in result)
    assert any("Nala" in info for info in result)
    assert any("Melman" in info for info in result)
    assert any("Dumbo" in info for info in result)

def test_search_animal_by_species(example_zoo):
    result = example_zoo.search_animal("Lejon")
    assert len(result) == 2  # Simba och Nala
    assert any("Simba" in r for r in result)
    assert any("Nala" in r for r in result)

    result = example_zoo.search_animal("Giraff")
    assert len(result) == 1
    assert "Melman" in result[0]

    result = example_zoo.search_animal("Tiger")
    assert result == "Inga djur av arten Tiger hittades."

def test_feed_animal(example_zoo):
    # Testa att Simba äter sin favoritmat
    simba = next(animal for animal in example_zoo.animals if animal.name == "Simba")
    simba.hungry = True  # Ställ in att Simba är hungrig
    result = example_zoo.feed_animal("Simba", "kött")
    assert result == "Simba sliter i sig kött med en kraftig riv!"
    assert simba.hungry is False  # Kontrollera att Simba inte längre är hungrig

    # Testa att Melman äter sin favoritmat
    melman = next(animal for animal in example_zoo.animals if animal.name == "Melman")
    melman.hungry = True  # Ställ in att Melman är hungrig
    result = example_zoo.feed_animal("Melman", "blad")
    assert result == "Melman sträcker sin långa hals för att nå blad."
    assert melman.hungry is False  # Kontrollera att Melman inte längre är hungrig

    # Testa att Simba vägrar mat som inte är favoritmat
    simba.hungry = True  # Gör Simba hungrig igen
    result = example_zoo.feed_animal("Simba", "gräs")
    assert result == "Simba rynkar på nosen och vägrar äta gräs."
    assert simba.hungry is True  # Kontrollera att Simba fortfarande är hungrig

    # Testa att ett djur som inte finns returnerar korrekt meddelande
    result = example_zoo.feed_animal("OkäntDjur", "kött")
    assert result == "Inget djur med namnet 'OkäntDjur' hittades."

def test_interact_with_animal(example_zoo):
    result = example_zoo.interact_with_animal("Dumbo")
    assert result == "Dumbo låter dig klappa dess snabel."

    result = example_zoo.interact_with_animal("Melman")
    assert result == "Melman sträcker sig efter blad."

    result = example_zoo.interact_with_animal("OkäntDjur")
    assert result == "Inget djur med namnet 'OkäntDjur' hittades."

def test_show_ticket_price(example_zoo):
    result = example_zoo.show_ticket_price()
    assert result == "Biljettpris: 100.0 SEK."

def test_show_addon_prices(example_zoo):
    result = example_zoo.show_addon_prices()
    assert "Mata djur: 50 SEK" in result
    assert "Detaljerad information: 30 SEK" in result

def test_add_to_cart_and_summarize(example_zoo):
    result = example_zoo.add_to_cart("Mata djur")
    assert result == "Tillvalet 'Mata djur' har lagts till i kundvagnen."

    result = example_zoo.add_to_cart("OkäntTillval")
    assert result == "Tillvalet 'OkäntTillval' är inte tillgängligt."

    summary = example_zoo.summarize_cart()
    assert "Mata djur" in summary
    assert "Totalpris: 50 SEK" in summary

def test_purchase(example_zoo):
    example_zoo.add_to_cart("Mata djur")
    result = example_zoo.purchase()
    assert result == "Köpet har slutförts. Tack för ditt besök!"

    summary = example_zoo.summarize_cart()
    assert summary == "Kundvagnen är tom."
