def sumN(n):
    if n == 0:
        return n
    return n + sumN(n-1)

n = int(input("Enter n: "))
print(sumN(n))