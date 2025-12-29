sum = 0

def reverse(n):
    global sum
    if n == 0:
        return
    
    sum = sum*10 + n%10
    reverse(n//10)

def palindrome(n):
    global sum
    
    return n == sum

n = int(input("Enter n: "))
reverse(n)
print(palindrome(n))


