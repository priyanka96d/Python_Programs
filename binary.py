import os
"""
filepath = "/Users/purva/Downloads/output-onlinetexttools.txt"
with open(filepath, 'rb') as binary_file:
    
    for line in binary_file:
        print(line,"\n")
    
    binary_file.seek(0, 0)  
    couple_bytes = binary_file.read(2)
    print(couple_bytes) 




file_length = os.path.getsize("/Users/purva/Downloads/output-onlinetexttools.txt")
print(file_length)


sam1_length = os.path.getsize("/Users/purva/Downloads/sample.3")
print(sam1_length)

sam2_length = os.path.getsize("/Users/purva/Downloads/sample.6")
print(sam2_length)
"""


def getGroupedAnagrams(words):
    # Write your code here
    sorted_list = []
    """
    for i in range(len(words)):
        print(words[i])
        for j in range(i+1,len(words)):
            print(words[j])
            if len(words[i]) == len(words[j]):
                sorted_list.append(words[i])  
            else:
                return 0
                
    
    new_list = []
    for i in words:
        print(i)
        i = sorted(i)
        print("sorted",i)
        sorted_list.append(i)

    for i in range(len(sorted_list)):
        for j in range(i+1,len(sorted_list)):
            if sorted_list[i] == sorted_list[j]:
                new_list.append(sorted_list[i])
                new_list.append(sorted_list[j])  
    print(new_list)                 

input_list = ['inch','cat','chin','kit','act']           
       
getGroupedAnagrams(input_list)
"""

str = 'hackthegame'



def countDis(str):
 
    # Stores all distinct characters
    s = set(str)
 
    # Return the size of the set
    return len(s)
 
 
# Driver Code
if __name__ == "__main__":
 
    # Given string S
    S = "hackthegame"
 
    print(countDis(S))    