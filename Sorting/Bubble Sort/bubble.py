def bubbleSortOptimized(arr):
    n = len(arr)    
    for i in range(n-1):
        isSorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                isSorted = False
        if isSorted == True:
            return arr
    return arr

def bubbleSort(arr):
    n = len(arr)    
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


import numpy as np

n = int(input("Enter size of array: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)
if len(arr)>n:
    print(f"Enter only {n} elements")
else:
    print(bubbleSortOptimized(arr))
