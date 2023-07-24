#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:33:33 2022

@author: purva
"""
#adding elements
class Queue:
    def __init__(self):
        self.queue = list()
        
        
    def addtoq(self,dataval): 
        # Insert method to add element
        if dataval not in self.queue: 
            self.queue.insert(0,dataval) 
            return True
        return False
    
    
# Pop method to remove element
    def removefromq(self): 
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No elements in Queue!")
    
    
TheQueue = Queue() 
TheQueue.addtoq("Mon") 
TheQueue.addtoq("Tue") 
TheQueue.addtoq("Wed") 
print(TheQueue.removefromq()) 
print(TheQueue.removefromq())
 
 
            