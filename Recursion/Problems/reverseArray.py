import numpy as np

rev = []

def reverseArr(arr, idx):
    global rev
    rev.append(arr[idx])
    if idx == 0:
        return    
    reverseArr(arr,idx-1)

# Using 2 pointers
def reverseArr2(arr, left, right):
    if left > right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverseArr2(arr, left+1, right-1)


arr = np.fromstring(input("Enter array elements: "), sep=" ", dtype= np.int32)
n = len(arr)

reverseArr(arr,n-1)
print(rev)

reverseArr2(arr,0, n-1)
print(arr)
