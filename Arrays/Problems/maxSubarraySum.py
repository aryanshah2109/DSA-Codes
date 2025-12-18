# Given an array of positives, negatives, zeroes, find maximum sum that any subarray of the array has
# Kadanes Algo

import numpy as np

def brute(arr):

    n = len(arr)
    maxSum = 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
        
            maxSum = max(sum, maxSum)
    
    return maxSum
        
def optimal(arr):
    # Kadanes Algo

    n = len(arr)
    sum = 0
    maxSum = float("-inf")

    for i in range(n):
        sum += arr[i]

        if maxSum < sum:
            maxSum = sum

        if sum < 0:
            sum = 0
    
    return maxSum
    

arr = np.fromstring(input("Enter array elements: "),sep=" ", dtype=np.int32)

print(brute(arr))
print(optimal(arr))
