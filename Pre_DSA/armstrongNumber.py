# check if number is armstrong number
def countDigits(n):
    digits = 0
    while(n>0):
        digits += 1
        n = n // 10
    return digits

def armstrongNumber(n):
    temp = n
    sum = 0
    digits = countDigits(n)
    while(temp>0):
        remainder = temp % 10
        sum += remainder**digits
        temp = temp // 10
    
    if sum == n:
        return True
    else:
        return False


n = int(input("Enter number to check if armstrong: "))

if(armstrongNumber(n)):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")