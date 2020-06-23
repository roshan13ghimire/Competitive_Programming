#Epic_Game
import math
a,b,n=map(int,input().split())
while True:
    n-=math.gcd(a,n)
    if(n<0):
        print(1)
        break
    n-=math.gcd(b,n)
    if(n<0):
        print(0)
        break
    
