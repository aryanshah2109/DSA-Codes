import numpy as np



def transpose(arr):

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows-1):
        for j in range(i+1, rows):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
            

    return arr

rows = int(input("Enter no of rows: "))
cols = int(input("Enter no of cols: "))

arr = []

print("Enter array elements:")
for i in range(rows):
    row = list(map(int,input().split()))
    arr.append(row)

print(arr)

print(transpose(arr))