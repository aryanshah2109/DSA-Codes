# leetcode 2
import numpy as np

def twoSum(arr:np.array,target:int):        
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] + arr[j] == target):
                return i,j
    return []

arr = np.array([])
n = int(input("Enter size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

target = int(input("Enter target: "))

indices = twoSum(arr,target)
print(indices)