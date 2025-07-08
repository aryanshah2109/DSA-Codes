# looped fibonacci series
def fibo(n):
    a = 0
    b = 1
    sum = 0
    for i in range(2,n+2):
        print(a,end=' ')
        sum = a + b
        a = b
        b = sum
        

n = int(input("Enter number of terms: "))
fibo(n)