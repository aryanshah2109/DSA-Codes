# Find out the first and last occurance of element x in a sorted array
# Eg: [1,1,3,4,5,5,5,7,9,10] , x = 5
# first occurance = idx 4, last occurance = idx 6

import numpy as np

# Approach 1: keep first and last = -1. Iterate through the array. if x found  and first ==-1 , 
# that is the first index. then continue checking and if found another element keep changing last

# TC = O(n)
def approach1(nums, target):

    n = len(nums)
    first = -1
    last = -1
    for i in range(n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
            
    return [first, last]

# Find lower bounds and upper bounds of that x
# first = arr[lower_bound] and last = arr[upper_bound - 1]
# also if x is not present, we have to handle that case too
def approach2(arr, x):
    n = len(arr)

    first = n
    last = n

    low = 0
    high = n-1

    # lower bound
    while low <= high:
        mid = low + int((high-low)/2)
        if arr[mid] >= x:
            high = mid - 1
            first = mid
        else:
            low = mid + 1
    
    low = 0
    high = n-1

    # upper bound
    while low <= high:
        mid = low + int((high-low)/2)
        if arr[mid] <= x:
            low = mid + 1
            last = mid
        else:
            high = mid - 1

    if first == n or arr[first] != x:
        first = -1
        last = -1

    return first, last



arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
x = int(input("Enter target: "))


first,last = approach1(arr,x)
print(first,last)

first,last = approach2(arr,x)
print(first,last)