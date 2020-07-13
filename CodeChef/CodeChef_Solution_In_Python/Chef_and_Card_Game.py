#Chef_and_Card_Game
for _ in range(int(input())):
    n=int(input())
    ch=0
    mo=0
    for _ in range(n):
        a,b=map(str,input().split())
        c=list(a)
        d=list(b)
        e=0
        f=0
        for i in range(len(c)):
            e+=int(c[i])
        for j in range(len(d)):
            f+=int(d[j])
        if(e>f):
            ch+=1
        elif(e<f):
            mo+=1
        else:
            ch+=1
            mo+=1
    if(ch>mo):
        print(0,ch)
    elif(ch<mo):
        print(1,mo)
    else:
        print(2,ch)
            
        
    