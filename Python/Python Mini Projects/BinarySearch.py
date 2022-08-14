# Binary search
"""
The goal of binary search is to search whether a given number is present in the string or not.

Topics: list,sorting,searching

Hint: First Check whether it is present in the middle or not then check for front and rear.

GIVE A TRY ON YOUR OWN

lst = [1,3,2,4,5,6,9,8,7,10]
lst.sort()
first=0
last=len(lst)-1
mid = (first+last)//2
item = int(input("enter the number to be search"))
found = False
while( first<=last and not found):
    mid = (first + last)//2
    if lst[mid] == item :
         print(f"found at location {mid}")
         found= True
    else:
        if item < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1 
   
if found == False:
    print("Number not found")
"""
import random

def binary_search(list, X):
    list = sorted(list)
    BN = list[int(len(list)//2)]
    while len(list) > 2 and BN != X and list[0] <= X <= list[int(len(list))-1]:
        while BN < X and len(list)>2:
            list = list[list.index(BN):]
            BN = list[int(len(list)/2)]
        while BN > X and len(list)>2:
            list = list[0:list.index(BN)]
            BN = list[int(len(list)/2)]
    if BN == X:
        print (f"Yes, {X} is in list")
    elif list[0] == X:
        print (f"Yes, {X} is in list")
    elif len(list) == 2:
        if list[1] == X:
            print (f"Yes, {X} is in list")
        elif list[0] == X:
            print (f"Yes, {X} is in list")
        else:
            print(f"No, {X} is not in list")
    else:
        print(f"No, {X} is not in list")

#list = list(range(1,101))
#random.shuffle(list)
list = [6, 7, 0, 9, 56, 76, 98, 88, 4, 45]
X = 56
binary_search(list, X)

