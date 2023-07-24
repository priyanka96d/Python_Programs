#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 09:14:06 2022

@author: purva
"""

from numpy import *

a = array([['Mon',18,20,22,17],
                ['Tue',11,18,21,18],
                ['Wed',15,21,20,19],
                ['Thu',11,20,22,21], 
                ['Fri',18,17,23,22],
                ['Sat',12,22,20,18], 
                ['Sun',13,15,19,16]])
m = reshape(a,(7,5)) 
print(m)

#accessing

print(m[2])
print(m[4][3])

#adding a row
m_r = append(m,[['Avg',12,15,13,'p']],0)
print(m_r)

#adding 
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(m_c)

#deletion a row
m = delete (m,[2],0)
print(m)

#deletion a col
m = delete(m,s_[2],1)
print(m)