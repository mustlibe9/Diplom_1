import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def empty_burger():
    return Burger()


@pytest.fixture
def default_bun():
    return Bun("White Bun", 100.0)


@pytest.fixture
def default_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0)


@pytest.fixture
def default_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)


@pytest.fixture
def cheese_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cheese", 40.0)
