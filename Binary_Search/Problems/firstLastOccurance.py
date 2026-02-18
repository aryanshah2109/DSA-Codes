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
    ## Optimal
    ## TC = O(logn) SC = O(1)
    first = n
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low) // 2
        if nums[mid] >= target:
            first = mid
            high = mid - 1
        else:
            low = mid + 1
    
    # If target not found
    if first == n or nums[first] != target:
        return [-1, -1]

    last = n
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low) // 2
        if nums[mid] > target:
            last = mid
            high = mid - 1
        else:
            low = mid + 1

    return [first, last-1]



arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
x = int(input("Enter target: "))


first,last = approach1(arr,x)
print(first,last)

first,last = approach2(arr,x)
print(first,last)
