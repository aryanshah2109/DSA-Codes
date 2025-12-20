# Given an array, return the elements that are the leaders in that array
# All element in subarray after the leaders must be smaller
# Eg: [3,15,2,5,12,9,4]
# Output: [15,12,9,4] -> all elements after 15 are less than 15. same for 12, 9 and 4


import numpy as np

# Brute: TC = O(n2) SC = O(n)

def brute(arr):
    n = len(arr)
    leaders = []

    for i in range(n):
        isLeader = True
        
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                isLeader = False
                break
        
        if isLeader:
            leaders.append(arr[i])

    return leaders


# Optimal: TC = O(n) SC = O(n)

def optimal(arr):
    n = len(arr)

    leaders = []

    max_element = float("-inf")

    for i in range(n-1,-1,-1):
        if arr[i] > max_element:
            leaders.append(arr[i])

        max_element = max(arr[i], max_element)

    return leaders


arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)

print(brute(arr))
print(optimal(arr))
