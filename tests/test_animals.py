import pytest
from animals.elephant import Elephant
from animals.lioncub import LionCub
from animals.giraffe import Giraffe
from animals.lion import Lion
from zoo.zoo import Zoo
from zoo.visitor import Visitor

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

# Fixturer för Zoo och Visitor
@pytest.fixture
def create_zoo():
    zoo = Zoo("Djurparken", "09:00-18:00", 100, {"Mata djur": 50, "Detaljerad info": 30})
    zoo.add_animal(Lion("Simba", 5, "assets/images/lion.png"))
    zoo.add_animal(Elephant("Dumbo", 10, "assets/images/elephant.png"))
    zoo.add_animal(Giraffe("Melman", 7, "assets/images/giraffe.png"))
    return zoo

@pytest.fixture
def create_visitor():
    return Visitor("Anna", 300)

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

# Tester för Zoo
def test_zoo_list_animals(create_zoo):
    animal_names = [animal.name for animal in create_zoo.animals]
    assert "Simba" in animal_names
    assert "Dumbo" in animal_names
    assert "Melman" in animal_names

def test_zoo_feed_animal(create_zoo):
    response = create_zoo.feed_animal("Simba", "kött")
    assert response == "Simba sliter i sig kött med en kraftig riv!"

def test_zoo_interact_with_animal(create_zoo):
    response = create_zoo.interact_with_animal("Dumbo", "klappa")
    assert response == "Dumbo låter dig klappa dess snabel."

# Tester för Visitor
def test_visitor_add_to_cart(create_visitor):
    create_visitor.add_to_cart("Mata djur", 50)
    assert len(create_visitor.cart) == 1
    assert create_visitor.budget == 250

def test_visitor_purchase(create_visitor):
    create_visitor.add_to_cart("Mata djur", 50)
    create_visitor.purchase()
    assert create_visitor.budget == 250
    assert len(create_visitor.cart) == 0
