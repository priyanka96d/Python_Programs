

inputData=[29,45,67,44,22,48,89,90,567,458,88,679,0,21,56,31,34,43,98,-97]
#create datafile of 20 integers.
with open('DataFile_test1.txt',mode='w') as index:                        
    for textdata in inputData:
        index.write(str(textdata))
        index.write('\n')
print("DataFile having 20 integers is created.")                        
        



file = open('DataFile_test1.txt', mode='r')#open datafile in read mode.
#convert datafile into list for performing opeartions.

numbers = [] #list
# logic for storing elements of datafile in a list.
for num in file: 
	digits = num.split()
	for i in digits:
	   numbers.append(int(i))


#loop to traverse each item in list
for i in range(len(numbers)):
    
    if numbers[i]%2==0:# logic for checking wheather item is even or odd.
        
        with open('even.txt',mode='a') as index: #create even.txt file for storing even numbers.
                index.write(str(numbers[i]))
                index.write('\n')

    else:
        with open('odd.txt',mode='a') as index: #create even.txt file for storing even numbers.
                index.write(str(numbers[i]))
                index.write('\n')
Even = open('even.txt', mode='r')
Odd = open('odd.txt', mode='r')
print("even.txt is created contain even numbers: \n%s"% Even.read())
print("odd.txt file is created contain odd numbers: \n%s"%Odd.read())




	   


