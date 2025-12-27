import numpy as np

"""
TC : 
    - Best Case -> O(nlogn)
    - Average Case -> O(nlogn)
    - Worst Case -> O(n2) : Already sorted

SC : O(n)

Recursive Relation:
    - Average Case / Best case -> T(n) = 2T(n/2) + O(n)
    - Worst Case -> T(n) = T(n-1) + O(n)

Unstable sort
"""

def partition(arr, low, high):
    pivot = arr[low]

    i = low + 1
    j = high

    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
        
    arr[j], arr[low] = arr[low], arr[j]
    return j


def quickSort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quickSort(arr, low, pivot_idx-1)
        quickSort(arr, pivot_idx+1, high)

arr = np.fromstring(input("Enter array elements: "), sep = " ", dtype=np.int32)

quickSort(arr,0,len(arr)-1)

print(arr)