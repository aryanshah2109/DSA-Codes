# Find out the peak element in an array
# The peak element is such which is greater than its left subarrays and right subarrays
# All the elements to the left of the peak are in sorted order and all to the right are in 
# reverse sorted order
# Eg: [0,1,2,5,8,9,3,4] -> Peak element = 9

import numpy as np

# Approach 1: Linear Search
# TC = O(n)
def approach1(nums):
    n = len(nums)

    for i in range(n-1):

        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i
        

# Approach 2: 
def approach2(nums):
    n = len(nums)
    low = 0
    high = n-1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[mid + 1]:
            low = mid + 1   # ascending
        else:
            high = mid      # descending or peak

    return low


nums = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)

print(approach1(nums))
print(approach2(nums))