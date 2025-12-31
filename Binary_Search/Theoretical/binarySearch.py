# TC = O(logn)

import numpy as np

def iterativeBinarySearch(arr:int,key):
    low = 0
    high = len(arr) -1

    while(low<=high):
        mid = low + int((high-low)/2)
        if(arr[mid] == key):
            return mid
        elif(arr[mid]>key):
            high = mid - 1
        else:
            low = mid + 1
    return -1

def recursiveBinarySearch(arr,low,high,key):
    if(low <= high):
        mid = low + int((high-low)/2)
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>key):
            return recursiveBinarySearch(arr,low,mid-1,key)
        else:
            return recursiveBinarySearch(arr,mid+1,high,key)
    return -1

n = int(input("Enter number of items: "))

arr = []
arr = np.fromstring(input("\nEnter elements: "),sep=' ',dtype=int)

key = int(input("\nEnter key element: "))

idxIterative = iterativeBinarySearch(arr,key)
if idxIterative == -1:
    print("Element not found!")
else:
    print(f"Element {key} found at idx: {idxIterative}")

idxRecursive = recursiveBinarySearch(arr,0,n-1,key)
if idxRecursive == -1:
    print("Element not found!")
else:
    print(f"Element {key} found at idx: {idxRecursive}")
