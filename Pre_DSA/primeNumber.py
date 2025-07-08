# prime number

def prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    flag = True
    for i in range(2,n//2):
        if n%i == 0:
            flag = False
    return flag

n = int(input("Enter number to check if prime: "))
if prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")