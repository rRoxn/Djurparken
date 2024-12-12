import pytest
import sys
import os

# Lägg till 'src'-mappen i Python-sökvägen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from zoo.zoo import Zoo  # Importera Zoo-klassen
from animals.lion import Lion
<<<<<<< HEAD
from animals.elephant import Elephant
from animals.lioncub import LionCub
from animals.giraffe import Giraffe

#Fixturer för djuren.
@pytest.fixture
def create_lion():
    return Lion("Simba", 5, "assets/images/lion.png")

@pytest.fixture
def create_elephant():
    return Elephant("Dumbo", 10, "assets/images/elephant.png")

@pytest.fixture
def create_giraffe():
    return Giraffe("Melman", 7, "assets/images/giraffe.png")

@pytest.fixture
def create_lioncub():
    return LionCub("Nala", 14, "assets/images/lioncub.png")
=======
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862

@pytest.fixture
def example_zoo():
    """Skapar ett exempel-zoo för tester."""
<<<<<<< HEAD
    zoo = Zoo(name="Test Zoo", opening_hours="10:00 - 16:00", ticket_price=100.0, addons={})
    zoo.add_animal(Lion("Simba", 5, "assets/images/lion.png"))
    zoo.add_animal(LionCub("Nala", 14, "assets/images/lioncub.png"))
    zoo.add_animal(Giraffe("Melman", 7, "assets/images/giraffe.png"))
    zoo.add_animal(Elephant("Dumbo", 10, "assets/images/elephant.png"))
=======
    zoo = Zoo(
        name="Test Zoo",
        opening_hours="10:00 - 16:00",
        ticket_price=100.0,
        addons={"Utfodring": 50.0, "Interaktiv tur": 75.0}
    )
    zoo.add_animal(Lion("Simba", 5, "images/lion.png"))  # Skicka med image_path
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862
    return zoo


def test_list_animals(example_zoo):
    animals = example_zoo.list_animals()
    assert len(animals) == 1
    assert "Lejon" in animals[0]

def test_search_animal_found(example_zoo):
    result = example_zoo.search_animal("Simba")
    assert "Lejon" in result

def test_search_animal_not_found(example_zoo):
    result = example_zoo.search_animal("OkäntDjur")
    assert "Inget djur med namnet" in result
