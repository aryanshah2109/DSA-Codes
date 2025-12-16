# Calculate sum of all subarrays of size k

import numpy as np

def brute(arr, k):
    n = len(arr)

    subarrays_sum = []

    for i in range(n-k+1):
        current_sum = 0
        for j in range(i, i+k):
            current_sum += arr[j]
        
        subarrays_sum.append(current_sum)
    
    return subarrays_sum

def optimal(arr, k):
    
    n = len(arr)

    i = 0
    j = 0

    subarrays_sum = []

    local_sum = 0

    while j<n:
        local_sum += arr[j]

        if j < i+k-1:
            j += 1
            continue

        subarrays_sum.append(local_sum)
        local_sum -= arr[i]
        i += 1
        j += 1
    
    return subarrays_sum

    

arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
k = int(input("Enter subarray size: "))

print(brute(arr,k))
print(optimal(arr,k))

