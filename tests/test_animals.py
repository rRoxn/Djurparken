import sys
import os
import pytest
from src.animals.elephant import Elephant
from src.animals.lioncub import LionCub
from src.animals.giraffe import Giraffe
from src.animals.lion import Lion

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Fixturer för djuren
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
    return LionCub("Nala", 14, "assets/images/lioncub.jpeg")


# Tester för get_info
def test_lion_get_info(create_lion):
    assert create_lion.get_info() == (
        "Art: Lejon, Namn: Simba, Ålder: 5, Favoritmat: kött, Bildväg: assets/images/lion.png"
    )

def test_elephant_get_info(create_elephant):
    assert create_elephant.get_info() == (
        "Art: Elefant, Namn: Dumbo, Ålder: 10, Favoritmat: jordnötter, Bildväg: assets/images/elephant.png"
    )

def test_giraffe_get_info(create_giraffe):
    assert create_giraffe.get_info() == (
        "Art: Giraff, Namn: Melman, Ålder: 7, Favoritmat: blad, Bildväg: assets/images/giraffe.png"
    )

def test_lioncub_get_info(create_lioncub):
    assert create_lioncub.get_info() == (
        "Lejonunge: Nala, Ålder: 1 år och 2 månader, Favoritmat: kött, Bildväg: assets/images/lioncub.jpeg"
    )


# Tester för eat
def test_lion_eat(create_lion):
    create_lion.hungry = True
    assert create_lion.eat("kött") == "Simba sliter i sig kött med en kraftig riv!"
    assert create_lion.hungry is False

def test_elephant_eat(create_elephant):
    create_elephant.hungry = True
    assert create_elephant.eat("jordnötter") == "Dumbo plockar upp jordnötter med snabeln och äter det långsamt."
    assert create_elephant.hungry is False

def test_giraffe_eat(create_giraffe):
    create_giraffe.hungry = True
    assert create_giraffe.eat("blad") == "Melman sträcker sin långa hals för att nå blad."
    assert create_giraffe.hungry is False

def test_lioncub_eat(create_lioncub):
    create_lioncub.hungry = True
    assert create_lioncub.eat("kött") == "Nala tuggar försiktigt på kött medan den leker."
    assert create_lioncub.hungry is False


# Tester för interact
def test_lion_interact(create_lion):
    assert create_lion.interact() == "Simba tittar stolt på dig."
    assert create_lion.hungry is True

def test_elephant_interact(create_elephant):
    assert create_elephant.interact() == "Dumbo låter dig klappa dess snabel."
    assert create_elephant.hungry is True

def test_giraffe_interact(create_giraffe):
    assert create_giraffe.interact() == "Melman sträcker sig efter blad."
    assert create_giraffe.hungry is True

def test_lioncub_interact(create_lioncub):
    assert create_lioncub.interact() == "Nala nafsar på ditt finger."
    assert create_lioncub.hungry is True


# Tester för bildväg
def test_lion_image_path(create_lion):
    assert create_lion.image_path == "assets/images/lion.png"

def test_elephant_image_path(create_elephant):
    assert create_elephant.image_path == "assets/images/elephant.png"

def test_giraffe_image_path(create_giraffe):
    assert create_giraffe.image_path == "assets/images/giraffe.png"

def test_lioncub_image_path(create_lioncub):
    assert create_lioncub.image_path == "assets/images/lioncub.jpeg"
