## Previous greater element
## IP - [6, 1, 5, 2, 8, 9, 3]
## OP - [-1, 6, 6, 5, -1, -1, 9]

## Brute
## TC = O(n2) SC = O(n)

nums = [6, 1, 5, 2, 8, 9, 3]
n = len(nums)
pge = [-1] * n

for i in range(n-1, -1, -1):
    hasPGE = False
    for j in range(i-1, -1, -1):
        if nums[j] > nums[i] :
            hasPGE = True
            pge[i] = nums[j]
            break
print(pge)
        
        
## Optimal
## TC = O(n) SC = O(2n)

nums = [6, 1, 5, 2, 8, 9, 3]
n = len(nums)
pge = [-1] * n
stack = []

for i in range(n):
    while len(stack) != 0 and stack[-1] <= nums[i]:
        stack.pop(-1)
    if len(stack) != 0:
        pge[i] = stack[-1]
    stack.append(nums[i])
print(pge)
    
    