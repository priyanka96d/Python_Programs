inputList = ['a','b','c','d']
"""
inputList.reverse()
print(inputList)

for i in reversed(inputList):
    print(i)
"""

inputStr = "123"
print(inputStr[::-1])

#print(inputList[::-1])
length = len(inputList)
print("length",length)
for x in inputStr[length:]:
    print(x)
    print(inputStr[x])