#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import pytest
from constant import Constant


class Food(Constant):

    class Fruit(Constant):
        id = 1
        name = "fruit"

        class Apple(Constant):
            id = 1
            name = "apple"

            class RedApple(Constant):
                id = 1
                name = "red apple"

            class GreenApple(Constant):
                id = 1
                name = "green apple"

        class Banana(Constant):
            id = 2
            name = "banana"

            class YellowBanana(Constant):
                id = 1
                name = "yellow banana"

            class GreenBanana(Constant):
                id = 2
                name = "green banana"

    class Meat(Constant):
        id = 2
        name = "meat"

        class Pork(Constant):
            id = 1
            name = "pork"

        class Meat(Constant):
            id = 2
            name = "meat"


def test_items():
    assert Food.items() == []
    assert Food.Fruit.items() == [("id", 1), ("name", "fruit")]
    assert Food.Fruit.Apple.items() == [("id", 1), ("name", "apple")]
    assert Food.Fruit.Apple.RedApple.items(
    ) == [("id", 1), ("name", "red apple")]


def test_collection():
    assert Food.collection() == [Food.Fruit, Food.Meat]
    assert Food.Fruit.collection() == [Food.Fruit.Apple, Food.Fruit.Banana]
    assert Food.Fruit.Apple.collection(
    ) == [Food.Fruit.Apple.GreenApple, Food.Fruit.Apple.RedApple]
    assert Food.Fruit.Apple.RedApple.collection() == []


def test_get_one():
    assert Food.get_one("id", 1) == Food.Fruit
    assert Food.get_one("name", "meat") == Food.Meat
    assert Food.get_one("value", "Hello World") is None


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
