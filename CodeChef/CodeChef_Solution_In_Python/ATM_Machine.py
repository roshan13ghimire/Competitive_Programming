#ATM_Machine
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=[]
    for i in range(len(a)):
        if(k<a[i]):
            l.append(0)
        else:
            k-=a[i]
            l.append(1)
    print(*l,sep='')