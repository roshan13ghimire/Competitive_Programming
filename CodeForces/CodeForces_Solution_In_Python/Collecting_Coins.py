#Collecting_Coins
import math
t=int(input())
for i in range(t):
    a,b,c,n=map(int,input().split())
    x=a+b+c+n
    y=x//3
    if((x%3==0) and a<=y and b<=y and c<=y):
        print("YES")
    else:
        print("NO")
    