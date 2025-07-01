import numpy as np

arr = np.array([])
n = int(input("Enter size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)
flag = True
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            flag = False
if(flag == False):
    print("Array is unsorted")
else:
    print("Array is sorted")