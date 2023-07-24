"""
a) If the array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.
b) If the array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.
c) If the array is {34, 23, 52, 12, 3}, then the function should return false because the elements are not consecutive.
d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive.

"""

import array as arr



def checking(array1):
    sort_array = sorted(array1)
    print("sorted array",sort_array,set(array1))
    if (len(array1) != len(set(array1))):
        return False
    else:
        for ele in range(len(sort_array)):
            if sort_array[ele+1] - sort_array[ele] == 1:
                return True
            else:
                return False    


if __name__=="__main__":
    array1 = arr.array('i',[5, 2, 3, 1, 4])
    print(checking(array1)) 

    array2 = arr.array('i',[83, 78, 80, 81, 79, 82])
    print(checking(array2))  

    

    array4 = arr.array('i',[7, 6, 5, 5, 3, 4])
    print(checking(array4))   
    array3 = arr.array('i',[34, 23, 52, 12, 3])
    print(checking(array3)) 