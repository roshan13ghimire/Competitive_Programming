#Frog_Jumping
import math
for _ in range(int(input())):
    a,b,k=map(int,input().split())
    if(k%2==0):
        c=a*(math.ceil(k/2))-b*(math.ceil(k//2))
    else:
        c=a*(math.ceil(k/2))-b*(math.floor(k//2))
    print(c)   