#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from const.test.validate_implementation import validate_implementation

def test():
    from const.test.creature_data import metadata
    from const.test.creature import creature_col
    validate_implementation(metadata, creature_col)
      
    from const.test.food_data import metadata
    from const.test.food import food_col
    validate_implementation(metadata, food_col)
       
    from const.test.inventory_data import metadata
    from const.test.inventory import inventory_col
    validate_implementation(metadata, inventory_col)
     
    from const.test.item_data import metadata
    from const.test.item import item_col
    validate_implementation(metadata, item_col)


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])