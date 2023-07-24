

def binarySearch(inputList,item):
    sortedList = sorted(inputList)
    midValue = round(len(sortedList)/2)
    print(sortedList[midValue])
    while(len(sortedList)):
        if item == sortedList[midValue]:
            print("item found")
        elif item > sortedList[midValue]:
            midValue += 1 
        elif item < sortedList[midValue]:
            midValue -= 1
        else:
            print("item Not Found")
if __name__ == "__main__":
    inputList = [1,3,4,6,2,8,9,7,10]
    binarySearch(inputList,7)