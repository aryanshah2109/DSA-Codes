# leetcode 75
## Brute Force -> sort using any sorting algorithm like merge sort
# TC = O(n*logn) SC = O(n)

## Better -> count number of 0s, 1s and 2s and then overwrite them accordingly
# TC = O(2*n) SC = O(1)
def sortColorsBetter(nums):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in nums:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(len(nums)):
        if(i < count0):
            nums[i] = 0
        elif(i < count1+count0):
            nums[i] = 1
        else:
            nums[i] = 2
    return nums

import numpy as np
n = int(input("Enter number of array elements: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ')
print(sortColorsBetter(arr))