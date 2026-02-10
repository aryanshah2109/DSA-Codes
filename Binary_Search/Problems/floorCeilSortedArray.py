import numpy as np
# Find the floor and ceil element of the sorted array given a sorted array and a target value
# Floor -> Largest element that is smaller than or equal to target
# Ceil -> Smallest element that is greater than or equal to target

# Eg:- [10 20 25 30 40] target = 21 -> floor = 20 ceil = 25
# Eg:- [10 20 30 40 50] target = 25 -> floor = 20 ceil = 30

def floor_ceil_array(arr: list, target: int):
    n = len(arr)
    idx = []
    
    ## Ceil
    ceil_idx = n
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] >= target:
            ceil_idx = mid
            high = mid - 1
        else:
            low = mid + 1

    ## Floor
    floor_idx = -1
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] <= target:
            floor_idx = mid
            low = mid + 1
        else:
            high = mid - 1
    
    ceil_element = arr[ceil_idx] if ceil_idx != n else float("inf")
    floor_element = arr[floor_idx] if floor_idx != -1 else float("-inf")

    if floor_element != float("-inf"):
            if ceil_element != float("inf"):
                return [int(floor_element), int(ceil_element)]
            else:
                return [int(floor_element), float("inf")]
    else:
            if ceil_element != float("inf"):
                return [float("-inf"), int(ceil_element)]
            


arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=int)
target = int(input("Enter target value: "))
print(floor_ceil_array(arr, target))
