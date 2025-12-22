# Given a matrix of 1s and 0s. Set the row and column to 0 whenever you encounter a zero element
'''
[
    [1,0,1],
    [1,1,1],
    [0,1,1]
]

O/P
[
    [0,0,0],
    [0,0,1],
    [0,0,0]
]

'''

import numpy as np
import copy

def markRow(arr, i, cols):
    for j in range(cols):
        if arr[i][j] != 0:
            arr[i][j] = -1

def markCol(arr, j, rows):
    for i in range(rows):
        if arr[i][j] != 0:
            arr[i][j] = -1


# Brute Force: 
# n -> rows, m -> cols
# TC = O((n*m)*(n+m) + O(n*m)) ==> O(n3)
# SC = O(1)
def brute(arr):
    rows = len(arr)
    cols = len(arr[0])

    # Mark -1 to those elements that are in a row or col of a 0 and will be marked later
    for i in range(rows):
        for j in range(cols):

            if arr[i][j] == 0:
                markRow(arr, i, cols)
                markCol(arr, j, rows)

    # Replace -1 with 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == -1:
                arr[i][j] = 0

    return arr

# Better TC = O(n*m) SC = O(n+m)
def better(arr):
    rows = len(arr)
    cols = len(arr[0])

    row_arr = np.zeros(rows)
    col_arr = np.zeros(cols)

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                row_arr[i] = 1
                col_arr[j] = 1

    for i in range(rows):
        for j in range(cols):
            if row_arr[i] == 1 or col_arr[j] == 1:
                arr[i][j] = 0
                 
    return arr




rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

arr = []

print("Enter array elements: ")
for i in range(rows):
    row = list(map(int,input().split()))
    arr.append(row)

arr1 = copy.deepcopy(arr)
arr2 = copy.deepcopy(arr)

print(brute(arr1))
print(better(arr2))