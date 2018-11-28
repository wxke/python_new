#!/usr/bin/env python
# -*- coding:UTF-8 -*-

name = input("name:")
age = input("age:")
info = '''
------------in fo -----------
name = {0}
age = {1}
'''.format(name,age)

print(info)

info2 = '''
name = {_name}
age = {_age}
'''.format(
    _name = name,
    _age = age
)
print(info2)