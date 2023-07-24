
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

    def atBeg(self,newNode):
        newNode =  Node(newNode)
        newNode.next = self.head
        self.head = newNode

    def middle(self, prevNode, newNode):

        if prevNode is None:
            print("previous node must be in linked list")
            return

        newData = Node(newNode)
        newData.next = prevNode.next  
        prevNode.next = newData

    def atEnd(self,newNode):
        newData = Node(newNode)

        if self.head is None:
            self.head = newData
            return

        iterator = self.head
        while(iterator.next):
            iterator = iterator.next
        iterator.next = newData        
         
    def delete(self,node):
        if self.head is None:
            pass
                 

if __name__ == "__main__":
    list1 = Linkedlist()
    list1.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node("Tue")
    

    list1.head.next = second
    second.next = fourth

    fourth.next = third
    #adding node in the first location
    list1.atBeg("Mon")

    #inserting nmode in middle
    list1.middle(second.next,"mid")

    #inserting at end
    list1.atEnd("end")
    #deleting node
    #list1.deleteNode()
    list1.printList()

   


