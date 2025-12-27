import numpy as np

"""
TC : 
    - Best Case -> O(n2)
    - Average Case -> O(n2)
    - Worst Case -> O(n2)

SC : O(1)

Unstable sort
"""



def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        minIdx = i
        
        for j in range(i+1,n):
            if arr[j] < arr[minIdx]:
                minIdx = j

        arr[i],arr[minIdx] = arr[minIdx], arr[i]

    return arr

arr = np.fromstring(input("Enter array elements: "), sep = " ", dtype=np.int32)
print(selectionSort(arr))