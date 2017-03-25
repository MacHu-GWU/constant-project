#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from constant.pkg.sixmini import PY3
from constant.test.validate_implementation import validate_implementation

def test():
    from constant.test.creature_data import metadata
    from constant.test.creature import creature_col
    validate_implementation(metadata, creature_col)
      
    from constant.test.food_data import metadata
    from constant.test.food import food_col
    validate_implementation(metadata, food_col)
    
    if PY3:
        from constant.test.inventory_data import metadata
        from constant.test.inventory import inventory_col
        validate_implementation(metadata, inventory_col)
         
        from constant.test.item_data import metadata
        from constant.test.item import item_col
        validate_implementation(metadata, item_col)


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])