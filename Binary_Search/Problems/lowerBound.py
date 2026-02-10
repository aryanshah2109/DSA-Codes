# Find out the lower bound of a given target
# A lower bound is the smallest index of the number greater than or equal to the target
# Eg: [1,3,4,6,9,13] and target = 5
#   |-> lower bound index = 3 as element at 3 = 6 and 6 is the first element greater than 5 i.e target
# If no smallest index found greater than or equal to target, return size of array

import numpy as np

# TC = O(logn)
def lowerBound(arr, target):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = low + int((high-low)/2)
        if arr[mid] >=  target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
        


arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
target = int(input("Enter target: "))
print(lowerBound(arr,target))