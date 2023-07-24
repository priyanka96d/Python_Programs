#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 14:08:24 2022

@author: purva
"""
import array
import json
obj = json.loads('{"gold": 1271, "silver":1284, "platinum":1270}')
print(obj['gold'])

print("silver", obj['silver'])


array1 = array('i', [10,11,22,34,11,90])

print("Array Elements:")
for x in array1:
    print(x)