#Chef_and_Subarrays
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    j=0
    for i in range(n):
        s=0
        t=1
        for k in range(i,n):
            s+=a[k]
            t*=a[k]
            if(s==t):
                j+=1
    print(j)