#Cutting_Recipes
import math
for _ in range(int(input())):
    a=list(map(int,input().split()))
    n=a[0]
    a.pop(0)
    if(n!=1):
        n1=a[0]
        n2=a[1]
        g=math.gcd(n1,n2)
        for i in range(2,len(a)):
            g=math.gcd(g,a[i])
        if(g==1):
            print(*a)
        else:
            for i in a:
                print(i//g,end=" ")
            print()
    else:
        print(*a)