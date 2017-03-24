#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

# from const.test.dev import food_example as food
# from const.test.dev.food_example import food_col

from const.test import food as food
from const.test.food import food_col


def test_items():
    assert food_col.keys() == []

    attrs = ["id", "name"]

    assert food_col.name____Fruit.keys() == attrs

    assert food_col.name____Fruit.name____Apple.keys() == attrs
    assert food_col.name____Fruit.name____Apple.name____red_apple.keys() == attrs
    assert food_col.name____Fruit.name____Apple.name____green_apple.keys() == attrs

    assert food_col.name____Fruit.name____Banana.keys() == attrs
    assert food_col.name____Fruit.name____Banana.name____yellow_banana.keys(
    ) == attrs
    assert food_col.name____Fruit.name____Banana.name____green_banana.keys(
    ) == attrs

    assert food_col.name____Meat.keys() == attrs
    assert food_col.name____Meat.name____Pork.keys() == attrs
    assert food_col.name____Meat.name____Beef.keys() == attrs


def test_auto_complete():
    # level 1 nest
    assert food_col.name____Fruit.id == 1
    assert food_col.name____Fruit.name == "Fruit"

    assert food_col.name____Meat.id == 2
    assert food_col.name____Meat.name == "Meat"

    # level 2 nest
    assert food_col.name____Fruit.name____Apple.id == 1
    assert food_col.name____Fruit.name____Apple.name == "Apple"
    assert food_col.name____Fruit.name____Banana.id == 2
    assert food_col.name____Fruit.name____Banana.name == "Banana"

    assert food_col.name____Meat.name____Pork.id == 1
    assert food_col.name____Meat.name____Pork.name == "Pork"
    assert food_col.name____Meat.name____Beef.id == 2
    assert food_col.name____Meat.name____Beef.name == "Beef"

    # level 3 nest
    assert food_col.name____Fruit.name____Apple.name____red_apple.id == 1
    assert food_col.name____Fruit.name____Apple.name____red_apple.name == "red apple"
    assert food_col.name____Fruit.name____Apple.name____green_apple.id == 2
    assert food_col.name____Fruit.name____Apple.name____green_apple.name == "green apple"

    assert food_col.name____Fruit.name____Banana.name____yellow_banana.id == 1
    assert food_col.name____Fruit.name____Banana.name____yellow_banana.name == "yellow banana"
    assert food_col.name____Fruit.name____Banana.name____green_banana.id == 2
    assert food_col.name____Fruit.name____Banana.name____green_banana.name == "green banana"

    # _collection
    assert len(food_col._collection) == 2

    assert len(food_col.name____Fruit._collection) == 2
    assert len(food_col.name____Fruit.name____Apple._collection) == 2
    assert len(food_col.name____Fruit.name____Banana._collection) == 2

    assert len(food_col.name____Meat._collection) == 2

    assert len(food_col._collection[0]._collection) == 2
    assert len(food_col._collection[0]._collection[0]._collection) == 2
    assert len(food_col._collection[0]._collection[1]._collection) == 2

    assert len(food_col._collection[1]._collection) == 2


def test_getattr_by_key_value():
    assert food_col.getattr_by_name("Fruit").id == 1
    assert food_col.getattr_by_name("Fruit").name == "Fruit"
    
    assert isinstance(food_col.getattr_by_name("Fruit"), food.Food)
    assert isinstance(food_col.name____Fruit.getattr_by_name("Apple"), food.Fruit)


if __name__ == "__main__":
    import os
    pytest.main(["--tb=native", "-s", os.path.basename(__file__)])
