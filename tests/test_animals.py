import pytest
import sys
import os

# Lägg till 'src'-mappen i Python-sökvägen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from animals.elephant import Elephant
from animals.lioncub import LionCub
from animals.giraffe import Giraffe
from animals.lion import Lion

# Tester för Lion
def test_lion_get_info():
    simba = Lion("Simba", 5, "images/lion.png")
    assert simba.get_info() == (
        "Lejon: Simba, Ålder: 5, Favoritmat: kött, Bildväg: images/lion.png"
    )

def test_lion_eat_specific():
    simba = Lion("Simba", 5, "images/lion.png")
    assert simba.eat("kött") == "Simba sliter i sig kött med en kraftig riv!"
    assert simba.hungry is False
    assert simba.eat("blad") == "Simba rynkar på nosen och vägrar äta blad."

def test_lion_image_path():
    simba = Lion("Simba", 5, "images/lion.png")
    assert simba.image_path == "images/lion.png"

# Tester för Elefant
def test_elephant_get_info():
    dumbo = Elephant("Dumbo", 10, "images/elephant.png")
    assert dumbo.get_info() == (
        "Elefant: Dumbo, Ålder: 10, Favoritmat: jordnötter, Bildväg: images/elephant.png"
    )

def test_elephant_interaction():
    dumbo = Elephant("Dumbo", 10, "images/elephant.png")
    assert dumbo.interact() == "Dumbo låter dig klappa dess snabel."
    assert dumbo.hungry is True

<<<<<<< HEAD

def test_elephant_feeding():
    dumbo = Elephant("Dumbo", 10)
    assert dumbo.feed("jordnötter") == "Dumbo åt upp jordnötter!"
=======
def test_elephant_eat_specific():
    dumbo = Elephant("Dumbo", 10, "images/elephant.png")
    assert dumbo.eat("jordnötter") == "Dumbo plockar upp jordnötter med snabeln och äter det långsamt."
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862
    assert dumbo.hungry is False
    assert dumbo.eat("kött") == "Dumbo trumpetar högt och vägrar äta kött."

<<<<<<< HEAD
#Tester för lejonunge
=======
def test_elephant_image_path():
    dumbo = Elephant("Dumbo", 10, "images/elephant.png")
    assert dumbo.image_path == "images/elephant.png"

# Tester för LionCub
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862
def test_lioncub_get_info():
    nala = LionCub("Nala", 14, "images/lioncub.png")
    assert nala.get_info() == (
        "Lejonunge: Nala, Ålder: 1 år och 2 månader, "
        "Favoritmat: kött, Bildväg: images/lioncub.png"
    )

def test_lioncub_interaction():
    simba_jr = LionCub("Simba Jr.", 8, "images/lioncub.png")
    assert simba_jr.interact() == "Simba Jr. tittar stolt på dig."
    assert simba_jr.hungry is True

<<<<<<< HEAD


def test_lioncub_feeding():
    """Testar matning av LionCub."""
    nala = LionCub("Nala", 14)
    assert nala.feed("kött") == "Nala åt upp kött!"  # Rätt mat
    assert nala.hungry is False  # Kontrollera att hungerstatus ändras
    assert nala.feed("blad") == "Nala vill inte äta blad."  # Fel mat
#Tester för giraff
=======
def test_lioncub_eat_specific():
    nala = LionCub("Nala", 14, "images/lioncub.png")
    assert nala.eat("kött") == "Nala tuggar försiktigt på kött medan den leker."
    assert nala.hungry is False
    assert nala.eat("blad") == "Nala vägrar äta blad och försöker leka istället."

def test_lioncub_image_path():
    nala = LionCub("Nala", 14, "images/lioncub.png")
    assert nala.image_path == "images/lioncub.png"

# Tester för Giraff
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862
def test_giraffe_get_info():
    melman = Giraffe("Melman", 7, "images/giraffe.png")
    assert melman.get_info() == (
        "Giraff: Melman, Ålder: 7, Favoritmat: blad, Bildväg: images/giraffe.png"
    )

def test_giraffe_interaction():
    melman = Giraffe("Melman", 7, "images/giraffe.png")
    assert melman.interact() == "Melman sträcker sig efter blad."
    assert melman.hungry is True

<<<<<<< HEAD



def test_giraffe_feeding():
    """Testar matning av Giraff."""
    melman = Giraffe("Melman", 7)
    assert melman.feed("blad") == "Melman åt upp blad!"
    assert melman.hungry is False  # Kontrollera att hungerstatus ändras
    assert melman.feed("kött") == "Melman vill inte äta kött."  # Fel mat
#Test för image_path
def test_elephant_interaction():
    dumbo = Elephant("Dumbo", 10, "images/elephant.png")
    assert dumbo.interact() == "Dumbo låter dig klappa dess snabel."
    assert dumbo.hungry is True

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
=======
def test_giraffe_eat_specific():
    melman = Giraffe("Melman", 7, "images/giraffe.png")
    assert melman.eat("blad") == "Melman sträcker sin långa hals för att nå blad."
    assert melman.hungry is False
    assert melman.eat("kött") == "Melman ignorerar kött och letar efter blad istället."

def test_giraffe_image_path():
    melman = Giraffe("Melman", 7, "images/giraffe.png")
    assert melman.image_path == "images/giraffe.png"
>>>>>>> 55ca0da80b47276ec6f744191dcf7b21d8368862
