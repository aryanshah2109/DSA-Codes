# leetcode 2
import numpy as np

def twoSumBrute(arr:np.array,target:int):   
    # tc = O(n^2)     
    # sc = O(1)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] + arr[j] == target):
                return i,j
    return []

def twoSumBetter(arr,k):
    # hashing
    # tc = O(n*logn)
    # sc = O(n)
    hashmap = dict()
    for i in range(len(arr)):
        if k-arr[i] in hashmap.keys():
            j = hashmap[k-arr[i]]
            return j,i
        else:
            hashmap.update({arr[i]:i})

def twoSumOptimal(arr, k):
    ### USE ONLY IF ARRAY IS SORTED. IF NOT THIS IS NOT OPTIMAL AS YOU HAVE TO SORT THE ARRAY FIRST
    # tc = O(n)
    # sc = O(1)
    left = 0
    right = n-1
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1



arr = np.array([])
n = int(input("Enter size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

target = int(input("Enter target: "))

print("Brute solution")
indices = twoSumBrute(arr,target)
print(indices)

print("Better solution")
indicesBetter = twoSumBetter(arr,target)
print(indicesBetter)

print("Optimal solution")
indicesOptimal = twoSumOptimal(arr,target)
print(indicesOptimal)