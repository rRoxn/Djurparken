import pytest
import sys
import os

# Lägg till 'src'-mappen i Python-sökvägen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from animals.elephant import Elephant

def test_elephant_interaction():
    dumbo = Elephant("Dumbo", 10)
    assert dumbo.interact() == "Dumbo låter dig klappa dess snabel."
    assert dumbo.hungry is True

def test_elephant_feeding():
    dumbo = Elephant("Dumbo", 10)
    assert dumbo.feed("jordnötter") == "Dumbo åt upp jordnötter!"
    assert dumbo.hungry is False
    assert dumbo.feed("kött") == "Dumbo vill inte äta kött."
