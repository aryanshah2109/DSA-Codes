import numpy as np

"""
TC : 
    - Best Case -> O(nlogn)
    - Average Case -> O(nlogn)
    - Worst Case -> O(nlogn)

SC : O(n)

Recursive relation: T(n) = 2T(n/2) + O(n)

Stable sort
"""

def merge(arr, low, mid, high):
    temp = []

    left = low
    right = mid+1

    while left <= mid and right <= high:

        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # Copy remaining elements
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    # copy temp back to arr
    for i in range(low, high+1):
        arr[i] = temp[i-low]



def mergeSort(arr, low, high):

    if low < high:
        mid = (low+high)//2

        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr,low,mid,high)
    
arr = np.fromstring(input("Enter array elements: "), sep = " ", dtype=np.int32)

mergeSort(arr,0,len(arr)-1)

print(arr)