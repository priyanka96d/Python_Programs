#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 09:37:43 2022

@author: purva
"""

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]) 
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months) 
print(Dates)

#accessing
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

for d in Days:
    print(d)
    

#adding items into sets
Days.add('Sun')
print(Days)

#removing item from a set
Days.discard('Sun')
print(Days)

#Union of sets
DaysA = set(["Mon","Tue","Wed"])
DaysB= set(["Wed","Thu","Fri","Sat","Sun"])
AllDays= DaysA|DaysB 
print(AllDays)

#intersection of Sets
AllDays= DaysA & DaysB 
print(AllDays)

#difference of sets
AllDays= DaysA - DaysB 
print(AllDays)

#compare sets
subsets= DaysA <= DaysB 
superSets = DaysB >= DaysA

print("SuperSets")
print(superSets)
print("subsets")
print(subsets)












