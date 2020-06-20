#beautiful_year
import sys
n=int(input())
m=n+1
while(True):
    a=str(n)
    b=str(m)
    s=set(b)
    if(len(s)==len(a)):
        print(m)
        sys.exit()
    m += 1