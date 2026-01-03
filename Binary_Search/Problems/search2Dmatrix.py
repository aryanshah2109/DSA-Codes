# Given a 2d matrix, return True/False whether a given target value exists in the matrix or not
# [[1,2,3],[4,5,6]] target = 4 -> True
# [[1,2,3],[7,8,9]] target = 5 -> False

import numpy as np

# Approach 1: O(n*m)
# Iterate through the entire matrix and search for the target

# Approach 2: O(n+log(m))
# Compare first and last element of each row with the target. if target lies between the first and
# last of a particular row, perform binary search on that row and return true or false

def binarySearch(arr, target):
    n = len(arr)

    low = 0
    high = n-1

    while low <= high:

        mid = low + (high-low)//2

        if arr[mid] == target:
            return True
        
        elif arr[mid] > target:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return False

def search2D(arr, target):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        if target >= arr[i][0] and target <= arr[i][m-1]:
            return binarySearch(arr[i], target)
    

# Approach 3: O(log(n*m))
# Suppose you have flattened the matrix into a 1D array. Then you can perform binary search on the
# flattened matrix. Now, instead of actually flattening it, use binary search and then find out 
# the row and col value. Then perform normal binary search operations on that row and col value
def search2Doptimized(arr, target):
    n = len(arr)
    m = len(arr[0])

    low = 0
    high = n*m - 1

    while low <= high:
        mid = low + (high-low)//2

        row = mid // m
        col = mid % m

        if arr[row][col] == target:
            return True
        elif arr[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False



n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

arr = []

print("Enter array elements: ")

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

target = int(input("Enter target: "))

if search2D(arr,target):
    print("Element found!")
else:
    print("Element not found")

if search2Doptimized(arr,target):
    print("Element found!")
else:
    print("Element not found")

