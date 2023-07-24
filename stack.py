#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:20:30 2022

@author: purva
"""

class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack: 
            self.stack.append(dataval) 
            return True
        else:
            return False
# Use peek to look at the top of the stack 
    def peek(self):
        return self.stack[-1]
    
    
# Use list pop method to remove element 
def remove(self):
    if len(self.stack) <= 0:
        return ("No element in the Stack")
    else:
        return self.stack.pop()


    
AStack = Stack() 
AStack.add("Mon") 
AStack.add("Tue") 
AStack.peek() 
print(AStack.peek())

AStack.add("Wed") 
AStack.add("purva") 
print(AStack.peek())

print(AStack.remove())
print(AStack.remove())