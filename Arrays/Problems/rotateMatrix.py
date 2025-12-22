import numpy as np

# Brute: TC = O(n2) SC = O(n2)
def rotateBrute(arr):

    rows = len(arr)
    cols = len(arr[0])
    
    ans = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):

            ans[j][rows-1-i] = arr[i][j]

    return ans

# Optimal: TC = O(n2) SC = O(1)
def rotateOptimal(arr):
    n = len(arr)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # Reverse each row using two pointers
    for i in range(n):
        left = 0
        right = n - 1

        while left < right:
            arr[i][left], arr[i][right] = arr[i][right], arr[i][left]
            left += 1
            right -= 1

    return arr


arr = []

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

print("Enter array elements: ")

for i in range(rows):
    row = list(map(int, input().split()))
    arr.append(row)

print(rotateBrute(arr))
print(rotateOptimal(arr))