#Movie_Weekend
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m=0
    r=0
    for i in range(n):
        if (a[i]*b[i])>=m:
            m=a[i]*b[i]
            if b[i]>r:
                r=b[i]
    for j in range(n):
        if r==b[j]:
            print(j+1)
            break
        
                