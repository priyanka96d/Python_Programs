#firtsArray = ['a','b','c']
#secondArray = ['a','b','d']

firtsArray = ['a','a','c',"e"]
secondArray = ['a','b','d']

unMatchedItem = []
"""
def compare(first,sec):
    for x,y in zip(first,sec):
        print(x,y)
        if x != y:
            unMatchedItem.append(y)
    return unMatchedItem , sec

"""

def compare(first,sec):
    #length = len(first)
    if len(first) != len(sec):
        unMatchedItem.append(first[len(first)-1])
    
    for x,y in zip(first,sec):
       
        if x != y:
            unMatchedItem.append(y)
    return unMatchedItem    

if __name__ == "__main__":
    print(compare(firtsArray,secondArray)   )         

