def sumDigits(n):
    if n == 0:
        return n
    return n%10 + sumDigits(n//10)

n = int(input("Enter n: "))
print(sumDigits(n))