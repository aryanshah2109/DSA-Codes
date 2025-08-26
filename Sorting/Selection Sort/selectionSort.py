
def selectionSort(arr):
    for i in range(n-1):
        minIdx = i
        for j in range(i+1,n):
            if arr[minIdx]>arr[j]:
                minIdx = j
        arr[minIdx],arr[i] = arr[i],arr[minIdx]
    return arr


        

import numpy as np
n = int(input("Enter number of elements: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

print(selectionSort(arr))