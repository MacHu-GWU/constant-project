#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.1"
__short_description__ = "Use IDLE autocomplete feature to manage large amount of constants."
__license__ = "MIT"
__author__ = "Sanhe Hu"

try:
    from .tpl.class_def import gencode
except:
    pass


import inspect


def get_attributes(klass):
    """Get all class attributes.
    """
    attributes = list()
    for attr, _ in inspect.\
            getmembers(klass, lambda x: not inspect.isroutine(x)):
        if not (attr.startswith("__") and attr.endswith("__")):
            attributes.append(attr)
    return attributes


class Constant(object):
    """A constant data collection.
    """
    
    @classmethod
    def items(cls):
        """Attributes ordered by alphabetical order.
        """
        l = list()
        for attr in get_attributes(cls):
            value = cls.__dict__[attr]
            try:
                if not issubclass(value, Constant):
                    l.append((attr, value))
            except:
                l.append((attr, value))
        return l
    
    @classmethod
    def keys(cls):
        return [attr for attr, _ in cls.items()]
    
    @classmethod
    def values(cls):
        return [value for _, value in cls.items()]
    
    @classmethod
    def to_dict(cls):
        return dict(cls.items())
    
    @classmethod
    def collection(cls):
        """Sub class ordered by alphabetical order.
        """
        l = list()
        for attr in get_attributes(cls):
            value = cls.__dict__[attr]
            try:
                if issubclass(value, Constant):
                    l.append(value)
            except:
                pass
        return l
    
    @classmethod
    def get_one(cls, attr, value):
        """Get a subclass that subclass.attr == value.
        """
        for klass in cls.collection():
            d = klass.__dict__
            try:
                if d[attr] == value:
                    return klass
            except:
                pass
        
        
if __name__ == "__main__":
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
        assert Food.Fruit.Apple.RedApple.items() == [("id", 1), ("name", "red apple")]
        
    test_items()
    
    def test_collection():
        assert Food.collection() == [Food.Fruit, Food.Meat]
        assert Food.Fruit.collection() == [Food.Fruit.Apple, Food.Fruit.Banana]
        assert Food.Fruit.Apple.collection() == [Food.Fruit.Apple.GreenApple, Food.Fruit.Apple.RedApple]
        assert Food.Fruit.Apple.RedApple.collection() == []
        
    test_collection()
    
    def test_get_one():
        assert Food.get_one("id", 1) == Food.Fruit
        assert Food.get_one("name", "meat") == Food.Meat
        assert Food.get_one("value", "Hello World") is None
        
    test_get_one()