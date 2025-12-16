# Find the first negative number in each subarray of the given array. 
# If a subarray has no negative numbers, return 0 for that subarray

import numpy as np

def firstNegativeSubarray(nums, k):
    n = len(nums)

    i = 0
    j = 0

    negatives = []
    subarrayIdx = 0
    while j<n:
        if nums[j] < 0:     # append negative number into list
            negatives.append(nums[j])
        
        if j < i+k-1:       # move j until window size is achieved
            j += 1
            continue

        if len(negatives) > 0:  # if there are elements in list, first negative = first element of list
            print(f"Subarray {subarrayIdx} negative number {negatives[0]}")
        else:
            print(f"Subarray {subarrayIdx} no negative number 0")
        
        if nums[i] < 0:     # remove the slided element from list before sliding the window
            negatives.pop(0)

        # slide the window
        i += 1
        j += 1
        subarrayIdx += 1 

nums = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)

k = int(input("Enter k: "))

firstNegativeSubarray(nums, k)