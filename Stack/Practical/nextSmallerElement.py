# Next smallest element

# IP = [6, 1, 5, 2, 8, 9, 3]

# OP = [1, -1, 2, -1, 3, 3, -1]

# If no nse, take -1

## Brute: TC = O(n2) SC = O(1)

nse = []
arr = [6, 1, 5, 2, 8, 9, 3]
n = len(arr)

for i in range(n):
    hasnse = False
    for j in range(i, n):
        if arr[j] < arr[i]:
            hasnse = True
            nse.append(arr[j])
            break
    if not hasnse:
        nse.append(-1)

print(nse)


## Optimal
# TC = O(n) SC = O(1)

arr = [6, 1, 5, 2, 8, 9, 3]
n = len(arr)

nse = [0] * n
stack = []

for i in range(n-1, -1, -1):
    while len(stack) != 0 and stack[-1] >= arr[i]:
        stack.pop(-1)
    if len(stack) == 0:
        nse[i] = -1
    else:
        nse[i] = stack[-1]
    stack.append(arr[i])
        
print(nse)
