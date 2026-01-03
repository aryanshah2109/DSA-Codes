# Find floor of square root of a number n
# Eg: n = 25, return 5
# Eg: n = 28, return 5

import numpy as np

# Approach 1: O(n)
# Manually go to each element from 1 -> n and check if its square is n

# Approach 2: O(logn)
# Binary Search from 1 -> n

def approach2(n):
    
    if n == 0:
        return 0


    low = 1
    high = n-1

    ans = 1

    while low <= high:

        mid = low + (high-low)//2

        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

print(approach2(25))
print(approach2(28))
print(approach2(36))