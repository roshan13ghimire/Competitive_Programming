#Primality_Test
def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
t=int(input())
for i in range(t):
    n=int(input())
    if(isPrime(n)==True):
        print("yes")
    else:
        print("no")
    