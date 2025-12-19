# Moore's Seating Algorithm

# Given an array, find out the element that appears for more than N/2
# Eg: [2,3,5,2,2,2] -> 2

import numpy as np

# Brute TC = O(n2) SC = O(1)
def brute(arr):
    n = len(arr)

    for i in range(n):
        count = 0
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                count += 1
        if count >= n//2:
            return arr[i]
    
    # No element > N/2?
    return -1

# Better TC = O(n*k) + O(n) SC = O(k) for k unique elements in array
def better(arr):
    n = len(arr)
    hashmap = {}

    for i in range(n):
        if arr[i] in hashmap:
            hashmap[arr[i]] += 1
        else:
            hashmap[arr[i]] = 1

    for element,count in hashmap.items():
        if count > n//2:
            return element

    # No element > N/2?
    return -1

# Optimal - Moore's Algo: TC = O(2n) SC = O(1)
def optimal(arr):
    n = len(arr)
    count = 0
    element = -1

    # Find out the element which appears most
    for i in range(n):
        if count == 0:
            count = 1
            element = arr[i]
        elif arr[i] == element:
            count += 1
        else:
            count -= 1
    
    # Find out if the element that appears most appears for > N/2 Times
    count_major_element = 0
    for i in range(n):
        if arr[i] == element:
            count_major_element += 1
    
    if count_major_element > n//2:
        return element
    
arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)

print(brute(arr))
print(better(arr))
print(optimal(arr))