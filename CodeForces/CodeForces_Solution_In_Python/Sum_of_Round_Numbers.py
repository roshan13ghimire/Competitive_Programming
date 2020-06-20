#Sum_of_Round_Numbers
t=int(input())
for _ in range(t):
    n=int(input())
    m=str(n)
    q=m.count('0')
    print(len(m)-q)
    b=n%10
    if(b!=0):
        print(b,end=' ')
    s=str(n)
    for i in range(1,len(str(n))):
        a=n-int(s[i:])
        if(a!=0):
            print(a,end=' ')
            n=int(s[i:])
            