#Alternating_subarray_prefix
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=[1]*n
    for i in range(len(a)-2,-1,-1):
        if (a[i]<0 and a[i+1]>0) or (a[i]>0 and a[i+1]<0):
            l[i]+=l[i+1]
    print(*l)