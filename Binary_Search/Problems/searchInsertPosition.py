# Given a sorted array and a target variable. If the target is in the array, return its index.
# If not, then find the index where it should be inserted so as to maintain the sorted order
# Eg:= [1,2,4,6] and target = 5 : output = 3 as when inserted at index 3 i.e [1,2,4,5,6] only then
# it will maintain sorted order

# We just have to find the lower bound of the target

import numpy as np

# TC = O(logn)
def searchInsertPosition(arr, target):
    low = 0
    high = len(arr) - 1
    idx = len(arr)
    while low <= high:
        mid = low + int((high-low)/2)
        if arr[mid] >= target:
            idx = min(idx, mid)
            high = mid - 1
        else:
            low = mid + 1
    return idx


arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
target = int(input("Enter target: "))
print(searchInsertPosition(arr,target))