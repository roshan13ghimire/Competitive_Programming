#Farmer_Feb
def isPrime(c):
    if(c>1):
        for i in range(2,c):
            if (c%i)==0:
                return False
                break
        else:
            return True
    else:
        return False
for _ in range(int(input())):
    x,y=map(int,input().split())
    i=1
    while(True):
        c=x+y+i
        i+=1
        if(isPrime(c)==True):
            print(i-1)
            break