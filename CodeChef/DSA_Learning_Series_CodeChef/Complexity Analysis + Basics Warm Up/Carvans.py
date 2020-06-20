#Carvans
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    s=a[0]
    for i in a:
        if(s>=i):
            c+=1
            s=i
    print(c)    