# rotate array by one place without creating a new array

import numpy as np

arr = np.array([])
n = int(input("Enter array size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

temp = arr[0]

for i in range(1,n):
    arr[i-1] = arr[i]
arr[n-1] = temp

print(arr)