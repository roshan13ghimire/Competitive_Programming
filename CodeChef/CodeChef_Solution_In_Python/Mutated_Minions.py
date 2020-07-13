#Mutated_Minions
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    for i in range(len(a)):
        d=k+a[i]
        b.append(d)
    c=0
    for i in range(len(b)):
        if(b[i]%7==0):
            c+=1
    print(c)        