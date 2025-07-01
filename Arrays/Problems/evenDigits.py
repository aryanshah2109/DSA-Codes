# leetcode 1295
# return amount of numbers with even digits in an array
import numpy as np

def findIfEven(n):
    count = 0
    while(n!=0):
        n //= 10
        count += 1
    return count
def findEvenDigits(arr):
    even = 0
    for i in range(len(arr)):
        if(findIfEven(arr[i]) %2 == 0):
            even += 1
    return even

arr = np.array([])
n = int(input("Enter size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

print(f"Number of even digits in {arr} are: {findEvenDigits(arr)}")

