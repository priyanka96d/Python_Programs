
from itertools import zip_longest


firstStr = 'add'
secStr = 'dad'

def anagram(str1,str2): 
	if len(firstStr) != len(secStr):
		return -1
	if sorted(firstStr) == sorted(secStr):
		return 1

res = anagram(firstStr,secStr)
if res == 1:
	print('string is anagram')
else:
    print("not anagram")    



firstList = ['cat', 'dog', 'tac', 'god', 'act','purva']
secList = ['cat', 'neha','purva']

sortedFirstList = []
sortedSecList = []
for a in firstList:
    print(a)
    sortedFirstList.append(sorted(a))

#print(sortedFirstList)

for b in secList:
    print(b)
    sortedSecList.append(sorted(b))

#print(sortedSecList)

for item in sortedSecList:
    if item in sortedFirstList:
        print("Anagram:",item)


def anagrams(word, words):     
    return filter(lambda x: sorted(word) == sorted(x), words)

op = anagrams('act',firstList)
print("final code:")
for i in op:
    print(i)    




def anagramGrp(lst):
	dict = {}
	for item in lst:
        sortedWords = ''.join(sorted(item))
        if sortedWords not in dict:
		    dict[sortedWords] = [item]
	    else:
		    dict[sortedWords].append(item)
	
	result = []

	for I in dict.values():
		result.append(I)    

