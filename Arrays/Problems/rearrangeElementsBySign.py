# Given an numsay of positives and negatives, numsange them in alternative order according to their sign
# Given that number of positives == negatives
# Do not change relative order of positives and negatives
# nums = [3,2,-1,4,-5,-9]
# Ans -> [3,-1,2,-5,4,-9]


import numpy as np

# Brute 
# TC = O(n) + O(n/2) 
# SC = O(n) as positives -> O(n/2) and negatives -> O(n/2)
def brute(nums):
    n = len(nums)

    positives = []
    negatives = []

    for i in range(n):  
        if nums[i] > 0:
            positives.append(nums[i])
        else:
            negatives.append(nums[i])

    for i in range(n//2):
        nums[2*i] = positives[i]
        nums[2*i + 1] = negatives[i]

    return nums

# Optimal
# TC = O(n)
# SC = O(n)
def optimal(nums):
    n = len(nums)
    
    positive_idx = 0
    negative_idx = 1
    
    renumsanged_elements = []

    for i in range(n):
        
        if nums[i] > 0:
            renumsanged_elements.insert(positive_idx, nums[i])
            positive_idx += 2
        
        else:
            renumsanged_elements.insert(negative_idx, nums[i])
            negative_idx += 2

    return renumsanged_elements


nums = np.fromstring(input("Enter numsay elements: "), sep = " ", dtype=np.int32)

print(brute(nums))
print(optimal(nums))