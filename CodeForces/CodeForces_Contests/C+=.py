#C+=
m=int(input())
for i in range(m):
    d=0
    a,b,n=map(int,input().split())  
    if(a>b):
        a,b=b,a
    while(b<=n):
        t=a+b
        a,b=b, t
        #print(t)
        d+=1
    print(d)    
