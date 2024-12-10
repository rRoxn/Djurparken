import pytest
import sys
import os

# Lägg till 'src'-mappen i Python-sökvägen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from animals.elephant import Elephant
from animals.lioncub import LionCub
from animals.giraffe import Giraffe

def test_elephant_interaction():
    dumbo = Elephant("Dumbo", 10)
    assert dumbo.interact() == "Dumbo låter dig klappa dess snabel."
    assert dumbo.hungry is True

def test_elephant_feeding():
    dumbo = Elephant("Dumbo", 10)
    assert dumbo.feed("jordnötter") == "Dumbo åt upp jordnötter!"
    assert dumbo.hungry is False
    assert dumbo.feed("kött") == "Dumbo vill inte äta kött."




def test_lioncub_get_info():
    """Testar get_info-metoden för LionCub."""
    nala = LionCub("Nala", 14)  # Skapa en ny instans för testet
    assert nala.get_info() == (
        "Lejonunge: Nala, Ålder: 1 år och 2 månader, Favoritmat: kött"
    )

def test_lioncub_interaction():
    """Testar interaktion med LionCub."""
    simba_jr = LionCub("Simba Jr.", 8)  # Ny instans, oberoende av main.py
    assert simba_jr.interact() == "Simba Jr. tittar stolt på dig."
    assert simba_jr.hungry is True  # Kontrollera att interaktion gör djuret hungrigt

def test_lioncub_feeding():
    """Testar matning av LionCub."""
    nala = LionCub("Nala", 14)
    assert nala.feed("kött") == "Nala åt upp kött!"  # Rätt mat
    assert nala.hungry is False  # Kontrollera att hungerstatus ändras
    assert nala.feed("blad") == "Nala vill inte äta blad."  # Fel mat

def test_giraffe_get_info():
    """Testar get_info-metoden för Giraff."""
    melman = Giraffe("Melman", 7)
    assert melman.get_info() == (
        "Giraff: Melman, Ålder: 7, Favoritmat: blad"
    )

def test_giraffe_interaction():
    """Testar interaktion med Giraff."""
    melman = Giraffe("Melman", 7)
    assert melman.interact() == "Melman sträcker sig efter blad."
    assert melman.hungry is True  # Kontrollera att giraffen blir hungrig

def test_giraffe_feeding():
    """Testar matning av Giraff."""
    melman = Giraffe("Melman", 7)
    assert melman.feed("blad") == "Melman åt upp blad!"
    assert melman.hungry is False  # Kontrollera att hungerstatus ändras
    assert melman.feed("kött") == "Melman vill inte äta kött."  # Fel mat