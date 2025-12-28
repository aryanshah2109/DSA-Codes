count = 0

def countZeroes(n):
    global count
    
    if n == 0:
        return
    
    remainder = n%10
    if remainder == 0:
        count += 1
        
    countZeroes(n//10)

n = int(input("Enter n: "))
countZeroes(n)
print(count)