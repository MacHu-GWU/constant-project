#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader

env = Environment(
    loader=PackageLoader('const', 'tpl'),
)
t_class_def = env.get_template("class_def.txt")
t_collection_class_def = env.get_template("collection_class_def.txt")
t_code = env.get_template("code.txt")