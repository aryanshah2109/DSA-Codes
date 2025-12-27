"""
TC : 
    - Best Case -> O(n)
    - Average Case -> O(n2)
    - Worst Case -> O(n2)

SC : O(1)

Stable sort
"""


import numpy as np

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j]>key:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key

    return arr

arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype=np.int32)
print(insertionSort(arr))