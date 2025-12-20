# Return number of subarrays with sum k
# Prefix sum

def numSubarrayBrute(nums,k):
    count = 0
    for i in range(len(nums)):
        sumSubarray = 0
        for j in range(i, len(nums)):
            sumSubarray += nums[j]

            if sumSubarray == k:
                count += 1
    return count

def numSubarrayPrefixSum(nums, k):
    prefixSum = {0: 1}
    count = 0
    sumSubarray = 0

    for i in range(len(nums)):
        sumSubarray += nums[i]
        remove = sumSubarray - k
        count += prefixSum.get(remove, 0)
        prefixSum[sumSubarray] = prefixSum.get(sumSubarray, 0) + 1

    return count


import numpy as np
nums = np.fromstring(input("Enter array: "),sep=' ',dtype=np.int32)
k = int(input("Enter k: "))

print(numSubarrayBrute(nums,k))

print(numSubarrayPrefixSum(nums,k))

