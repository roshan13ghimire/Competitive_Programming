#Park_Lighting
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if(n%2==0):
        print(m*(n//2))
    elif(m%2==0):
        print(n*(m//2))
    else:
        print(m*(n//2)+(m//2)+1)