#Chef_and_Price_Control
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    for i in range(len(a)):
        if(a[i]>k):
            a[i]=k
    print(s-sum(a))