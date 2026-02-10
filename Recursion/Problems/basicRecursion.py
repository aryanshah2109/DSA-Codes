# print n -> 1
def printNTo1(n):
    if n == 0:
        return
    print(n, end=" ")
    printNTo1(n-1)

def print1ToN(n):
    if n == 0:
        return
    print1ToN(n-1)
    print(n, end=" ")
    
def reverseArray(arr: list, start, end):
    if start > end:
        return arr
        
    arr[start], arr[end] = arr[end],arr[start]
    start = start + 1
    end = end - 1
    return reverseArray(arr, start, end)
    
def reverseString(s: str, ans: str, idx: int):
    if idx == len(s):
        return ans
    ans += s[len(s)-idx-1]
    idx += 1
    
    return reverseString(s, ans, idx)

def calculateSum(n:int, sum_n:int):
    if n == 0:
        return sum_n
    sum_n += n
    return calculateSum(n-1, sum_n)
 
    
printNTo1(10)
print("\n")

print1ToN(10)
print("\n")

arr = reverseArray([1,2,3,4,5], 0, 4)
print(arr)

ans = reverseString("abcdef", "", 0)
print(ans)

sum_n = calculateSum(5, 0)
print(sum_n)