#Maximum_GCD
import math
for _ in range(int(input())):
    n=int(input())
    if(n%2==0):
        print(int(n//2))
    else:
        print(int((n-1)//2))            
                
        