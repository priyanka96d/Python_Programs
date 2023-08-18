# Find the thrid occurence of given number.

"""
First count occuence of given number. If smaller than 3 return NULL.
Check if list contains ele or not.
"""

my_list = [10, 20, 30, 20, 66, 80, 20, 20]
op = []
cnt  = 1
for ind, item in enumerate(my_list):
    if item == 20:
        print(ind,item)
        if cnt == 3:
            
            op.append(ind)
        cnt = cnt+1
        
print(op)