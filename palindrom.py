
"""
def isPalindrom(x):
    temp = x
    reverseNum = 0
    while(x>0):
            remainder = x % 10
            reverseNum = reverseNum * 10 + remainder
            x = x//10
            
    print(reverseNum)
    if (temp == reverseNum):
        return True
    else:
        return False


if __name__ == "__main__":
    print(isPalindrom(-121))     

"""

#Single Linked List       
from email import header
from typing import Optional


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None    

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

def isPalindrom(self, head:Optional[Node]):
    val = []
    current = head

    while(current is not None):
        val.append(current.data)
        current.next = current

    if val == val[::-1]:
        return True
    else: return False



if __name__ == "__main__":
    list1 = Linkedlist()
    list1.head = Node(1)
    second = Node(2)
    thrid = Node(1)

    list1.head.next = second
    second.next = thrid

    list1.printList()
    
    isPalindrom() 
