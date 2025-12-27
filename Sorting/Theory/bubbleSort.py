import numpy as np

"""
TC : 
    - Best Case -> O(n)
    - Average Case -> O(n2)
    - Worst Case -> O(n2)

SC : O(1)

Stable sort
"""

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    
    return arr

def bubbleSortOptimized(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            return arr
    
    return arr


arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=np.int32)
print(bubbleSort(arr.copy()))
print(bubbleSortOptimized(arr.copy()))