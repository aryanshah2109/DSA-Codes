import numpy as np
n = int(input("Enter array size: "))
arr = np.array([])
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

def reverse(arr, i ,j):
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    return arr

k = int(input("Enter number of steps: "))
if k>n:
    k %= n
arr = reverse(arr,0,n-1)
arr = reverse(arr,0,k)
arr = reverse(arr,k+1,n-1)
print(arr)