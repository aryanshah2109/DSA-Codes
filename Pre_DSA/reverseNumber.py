# reverse a number
def reverse(n:int):
    rev = 0
    r = 0
    while(n>0):
        r = n%10
        rev = rev + r
        rev = rev * 10
        n = n//10
    return rev//10


n = int(input("Enter a number: "))
print(reverse(n))

