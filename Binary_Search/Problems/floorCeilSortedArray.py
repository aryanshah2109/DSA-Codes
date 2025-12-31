# Find the floor and ceil of the sorted array given a sorted array and a target value
# Floor -> Largest element that is smaller than or equal to target
# Ceil -> Smallest element that is greater than or equal to target

# Eg:- [10 20 25 30 40] target = 21 -> floor = 20 ceil = 25
# Eg:- [10 20 30 40 50] target = 25 -> floor = 20 ceil = 30

import numpy as np


def floorCeilArray(arr, target):
    low = 0 
    high = len(arr) - 1   
    ans = len(arr)

    while low <= high:
        mid = low + int((high-low)/2)

        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    ceil = arr[ans] if ans < len(arr) else None

    low = 0 
    high = len(arr) - 1   
    ans = -1

    while low <= high:
        mid = low + int((high-low)/2)
        if arr[mid] <= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    floor = arr[ans] if ans >= 0 else None

    return floor, ceil



arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
target = int(input("Enter target: "))

floor, ceil = floorCeilArray(arr, target)
print(floor)
print(ceil)