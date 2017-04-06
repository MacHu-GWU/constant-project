#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from __future__ import print_function
import pytest
from constant import Constant
from constant.pkg.sixmini import PY3


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
                id = 2
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
        sort_by="__name__") == [Food.Fruit.Apple.GreenApple, Food.Fruit.Apple.RedApple]
    assert Food.Fruit.Apple.collection(
        sort_by="name") == [Food.Fruit.Apple.GreenApple, Food.Fruit.Apple.RedApple]
    assert Food.Fruit.Apple.collection(
        sort_by="id") == [Food.Fruit.Apple.RedApple, Food.Fruit.Apple.GreenApple]
    assert Food.Fruit.Apple.collection(sort_by="id", reverse=True) == [
        Food.Fruit.Apple.GreenApple, Food.Fruit.Apple.RedApple]
    assert Food.Fruit.Apple.RedApple.collection() == []


def test_get_one():
    assert Food.get("id", 1) == Food.Fruit
    assert Food.get("name", "meat") == Food.Meat
    assert Food.get("value", "Hello World") is None
    assert Food.get("id", 1, multi=True) == [Food.Fruit, ]


def test_get_one_performance():
    import time
    
    st = time.clock()
    for i in range(1000):
        Food.get("id", 2)
    elapsed = time.clock() - st
    if PY3:
        print("with lfu_cache elapsed %.6f second." % elapsed)
    else:
        print("without cache elapsed %.6f second." % elapsed)
            
    
            
if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
