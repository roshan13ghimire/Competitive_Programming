#Lazy_Zem
for _ in range(int(input())):
    n,b,m=map(int,input().split())
    ans=0
    while n>0:
        if n%2!=0:
            temp=(n+1)//2
        else:
            temp=n//2
        ans+=temp*m
        ans+=b
        m*=2
        n-=temp
    print(ans-b)
            