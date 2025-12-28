def reverse(n):
    if n%10 == n:   # Last digit
        print(n)
        return
    
    print(n%10, end="")
    reverse(n//10)


n = int(input("Enter n: "))
reverse(n)