#Minimal_Square
import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    m=max(a,b)
    mi=min(a,b)
    if(m>2*mi):
        print(m*m)
    else:
        print((2*mi)*(2*mi))