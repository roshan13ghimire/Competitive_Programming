#Packaging_Cupcakes
import math
t=int(input())
for i in range(t):
    n=int(input())
    if(n%2==0):
        print(int(n/2)+1)
    else:
        print(int((n+1)/2))