# Calculate average of each subarray of size k

import numpy as np

def brute(arr, k):
    n = len(arr)

    averages = []
    
    for i in range(n-k+1):

        sum = 0

        for j in range(i, i+k):

            sum += arr[j]
        
        averages.append(sum//k)
    
    return averages

def optimal(arr, k):
    n = len(arr)

    i = 0
    j = 0
    
    averages = []

    sum_val = 0
    
    while j<n:
        sum_val += arr[j]

        if j < i+k-1:
            j += 1
            continue

        averages.append(sum_val//k)

        sum_val -= arr[i]

        i += 1
        j += 1
    
    return averages
        


arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
k = int(input("Enter subarray size: "))

print(brute(arr,k))
print(optimal(arr,k))