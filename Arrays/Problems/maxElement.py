import numpy as np
arr = np.array([])
n = int(input("Enter size of array: "))

arr = np.fromstring(input("Enter elements: "),sep=' ',dtype=int)
print(arr)
max = arr[0]
for j in arr:
    if(max<j):
        max = j
print(f"Maximum element: {max}")
