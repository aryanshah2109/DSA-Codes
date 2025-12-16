# Calculate number of subarrays of size k with given sum x
import numpy as np

def brute(arr, k, sum):
    n = len(arr)

    count = 0

    for i in range(n-k+1):
        local_sum = 0
        for j in range(i, i+k):
            local_sum += arr[j]

        if local_sum == sum:
            count += 1
    return count

def optimal(arr, k, sum):
    
    n = len(arr)

    i = 0
    j = 0

    count = 0
    local_sum = 0

    while j<n:
        local_sum += arr[j]

        if j < i+k-1:
            j += 1
            continue
    
        if local_sum == sum:
            count += 1
        
        local_sum -= arr[i]
        i += 1
        j += 1
    
    return count


arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
k = int(input("Enter subarray size: "))
sum = int(input("Enter sum: "))

print(f'Counts of sum {sum} : {brute(arr,k,sum)}')
print(f'Counts of sum {sum} : {optimal(arr,k,sum)}')
