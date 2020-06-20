#Phoenix_and_Balance
t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    c=0
    b=0
    for i in range(1,n+1):
        l.append(2**i)
    #print(l)
    for i in range(n//2-1):
        c+=l[i]
    c+=l[n-1]
    #print(c)
    for i in range(n//2-1,n-1):
        b+=l[i]
    #print(b)    
    print(abs(c-b))    