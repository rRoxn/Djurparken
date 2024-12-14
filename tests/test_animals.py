import pytest
import sys
import os

# Lägg till 'src'-mappen i Python-sökvägen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from animals.elephant import Elephant
from animals.lioncub import LionCub
from animals.giraffe import Giraffe
from animals.lion import Lion

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

# Tester för Lion
def test_lion_get_info(create_lion):
    assert Lion.get_info() == (
        "Lejon: Simba, Ålder: 5, Favoritmat: kött, Bildväg: images/lion.png"
    )

def test_lion_eat_specific(create_lion):
    
    assert Lion.eat("kött") == "Simba sliter i sig kött med en kraftig riv!"
    assert Lion.hungry is False
    assert Lion.eat("blad") == "Simba rynkar på nosen och vägrar äta blad."

def test_lion_image_path(create_lion):
    
    assert Lion.image_path == "images/lion.png"

# Tester för Elefant
def test_elephant_get_info(create_elephant):
    
    assert Elephant.get_info() == (
        "Elefant: Dumbo, Ålder: 10, Favoritmat: jordnötter, Bildväg: images/elephant.png"
    )

def test_elephant_interaction(create_elephant):
    
    assert Elephant.interact() == "Dumbo låter dig klappa dess snabel."
    assert Elephant.hungry is True


def test_elephant_feeding(create_elephant):
    
    assert Elephant.feed("jordnötter") == "Dumbo åt upp jordnötter!"
    assert Elephant.hungry is False
    assert Elephant.eat("kött") == "Dumbo trumpetar högt och vägrar äta kött."

#Tester för lejonunge
def test_lioncub_get_info(create_lioncub):
    
    assert LionCub.get_info() == (
        "Lejonunge: Nala, Ålder: 1 år och 2 månader, "
        "Favoritmat: kött, Bildväg: images/lioncub.png"
    )

def test_lioncub_interaction(create_lioncub):
    
    assert LionCub.interact() == "Simba Jr. tittar stolt på dig."
    assert LionCub.hungry is True

def test_lioncub_eat_specific(create_lioncub):
    
    assert LionCub.feed("kött") == "Nala tuggar försiktigt på kött medan den leker."
    assert LionCub.hungry is False
    assert LionCub.eat("blad") == "Nala vägrar äta blad och försöker leka istället."

def test_lioncub_image_path(create_lioncub):
    
    assert LionCub.image_path == "images/lioncub.png"

# Tester för Giraff
def test_giraffe_get_info(create_lioncub):
    
    assert LionCub.get_info() == (
        "Giraff: Melman, Ålder: 7, Favoritmat: blad, Bildväg: images/giraffe.png"
    )

def test_giraffe_interaction(create_giraffe):
    
    assert Giraffe.interact() == "Melman sträcker sig efter blad."
    assert Giraffe.hungry is True




def test_giraffe_feeding(create_giraffe):
    """Testar matning av Giraff."""
    
    assert Giraffe.feed("blad") == "Melman åt upp blad!"
    assert Giraffe.hungry is False  # Kontrollera att hungerstatus ändras
    assert Giraffe.feed("kött") == "Melman vill inte äta kött."  # Fel mat
#Test för image_path
def test_elephant_interaction(create_elephant):
    
    assert Giraffe.interact() == "Dumbo låter dig klappa dess snabel."
    assert Giraffe.hungry is True

def test_elephant_image_path():
    dumbo = Elephant("Dumbo", 10, "images/elephant.png")
    assert dumbo.image_path == "images/elephant.png"

def test_lioncub_image_path():
    nala = LionCub("Nala", 14, "images/lioncub.png")
    assert nala.image_path == "images/lioncub.png"

def test_giraffe_interaction():
    melman = Giraffe("Melman", 7, "images/giraffe.png")
    assert melman.interact() == "Melman sträcker sig efter blad."
    assert melman.hungry is True
