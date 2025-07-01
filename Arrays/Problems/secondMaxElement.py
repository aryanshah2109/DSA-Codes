import numpy as np

arr = np.array([])
n = int(input("Enter array size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

max = arr[0]
smax = arr[0]
for i in arr:
    if(max<i):
        smax = max
        max = i

print(f"Max: {max} and Second max: {smax}")