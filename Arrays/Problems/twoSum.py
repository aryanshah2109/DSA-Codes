# leetcode 2
import numpy as np

def twoSumBrute(arr:np.array,target:int):        
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] + arr[j] == target):
                return i,j
    return []

def twoSumBetter(arr: np.array, target: int):
    # hashing
    hashtable = dict()
    for nums in arr:
        if nums in hashtable.keys:
            hashtable[nums] += 1
        else:
            hashtable.update({nums:1})
    print(hashtable)


arr = np.array([])
n = int(input("Enter size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

target = int(input("Enter target: "))

indices = twoSumBrute(arr,target)
print(indices)

twoSumBetter(arr,target)