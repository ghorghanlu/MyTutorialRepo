# Binary search
"""
Binary search
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

def binary_search(x, list):
    list.sort()
    low = 0
    high = len(list)-1
    SearchCompleted = False
    while low<=high and not SearchCompleted:
        mid = (low + high)//2
        if list[mid] == x:
            print(f"{x} found at position {mid}")
            SearchCompleted = True
        else:
            if x > list[mid]:
                low = mid + 1
            else:
                high = mid - 1 
    if SearchCompleted == False:
        print(f"The number {x} was not in the list")

list = [9, 10, 6, 3, 4, 8, 93, 100, 4565,63, 0, 23, 21, 22, 24] # Our desired list
x = 8 # The number we want to know if it is in the list or not

binary_search(8, list)
