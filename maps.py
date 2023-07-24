#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 10:01:16 2022

@author: purva
"""

import collections

dict1 = {'days1': 'Mon','days2': 'Tue'}
dict2  = {'days3': 'Wed', 'day1':'Thu'}

res = collections.ChainMap(dict1,dict2)

#single dict
print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

#print all the ele from the result
print('elements')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()    