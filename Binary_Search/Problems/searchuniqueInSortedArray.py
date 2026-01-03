# Given a sorted array with all elements appearing twice except one, find the unique element
# Eg: [1,1,2,3,3,4,4,5,5] -> 2

import numpy as np

# Approach 1: Linear Search TC=O(n2) SC=O(1)
# Search each element and whether it is unique

# Approach 2: Hashing TC=O(n) SC=O(n/2)
# Create a hashtable with occurances of each element and return the key with value 1

# Approach 3: Binary Search TC=O(logn) SC=O(1)



def searchUnique(arr):
    n = len(arr)

    low = 0
    high = n-1

    # single element array
    if n == 1:
        return arr[0]

    while low <= high:
        mid = low + (high-low)//2

        # Edge cases
        if mid == 0 and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        elif mid == n-1 and arr[mid] != arr[mid-1]:
            return arr[mid]

        # mid is the unique element
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        elif arr[mid] == arr[mid-1]:
            if mid % 2 == 0:
                high = mid - 1
            else:
                low = mid + 1
        
        else:
            if mid % 2 == 0:
                low = mid + 1                
            else:
                high = mid - 1
    
    return arr[low]


arr = np.fromstring(input("Enter array elements: "), sep=" ",dtype=int)
print(searchUnique(arr))