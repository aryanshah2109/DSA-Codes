# for a window of fixed size k for an array nums, give maximum sum of the k sized window

import numpy as np

def maxSumFixWindow(nums,k):
    i = 0
    j = 0
    n = len(nums)
    maxSum = 0
    sum = 0
    while j < n:
        sum += nums[j]

        if j < i + k - 1:
            j += 1

        else:
            maxSum = max(sum,maxSum)
            sum -= nums[i]
            i += 1
            j += 1
            
    return maxSum

nums = np.fromstring(input("Enter array elements: "),sep=' ',dtype=np.int32)
k = int(input("Enter window size: "))

maxSum = maxSumFixWindow(nums,k)

print(f"Maximum sum for window size {k} is {maxSum}")       