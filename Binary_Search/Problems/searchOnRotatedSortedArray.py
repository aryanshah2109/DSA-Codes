# Given a rotated sorted array, find out the index of the given target value
# A rotated sorted array is when a few elements of a sorted array are rotated to the front of the array
# Eg: [5,6,7,0,1,2,3,4]

# Approach 1: Linear Search for target on arr
# TC = O(n)

# Approach 2: Binary Search
# Core binary search will not apply here as in core binary search we eliminate one half of the array
# based on knowing that the element will not lie in that eliminated half.
# Eg: [1,2,3,4,5,6] and target = 5. We know that for arr[mid] = 3, 3 < 5 and so if the array is sorted,
# then the target 5 will not lie in the first half. So we can eliminate the first half
# But in this problem, [5,6,7,0,1,2,3,4] and target = 5, for arr[mid] = 0 and 0 < 5. We cannot say that 
# as 0 < 5, 5 will lie to the right of the array so eliminate left half due to the rotated array.
# so core binary search will not apply here.
# 
# What we can do is that in a rotated sorted array, any one of the half will be sorted i.e. 
# after rotation, either the array from low->mid (left half) or the array from mid->high (right half)
# will be sorted. So we need to first find out whether the left half is sorted or the right half is
# After finding that out, we can apply binary search on that half. Suppose the left half is sorted. 
# If the element is in that sorted half then it will be arr[low] <= target <= arr[mid]. 
# if this is not true then it must lie on the right half that is unsorted. So iterate again in the 2nd half

import numpy as np

def approach2(nums, target):
    n = len(nums)

    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high-low)//2

        if nums[mid] == target:
            return mid
        
        # Find out if left sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # right sorted
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1 

    return -1        
    
nums = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
target = int(input("Enter target: "))

print(approach2(nums, target))