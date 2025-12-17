# Given an array arr and sum k, find size of smallest subarray with sum greater than or equal to k

import numpy as np


def optimal(arr, k):
    n = len(arr)
    
    i = 0
    j = 0

    min_window_size = float("inf")

    local_sum = 0

    while j<n:
        local_sum += arr[j]

        while local_sum >= k:
            current_window_size = j - i + 1

            min_window_size = min(current_window_size, min_window_size)
           
            local_sum -= arr[i]
            i += 1                           
            
        j += 1
    
    return 0 if min_window_size == float("inf") else min_window_size

arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
k = int(input("Enter sum k: "))

min_window_size = optimal(arr, k)
print(min_window_size)