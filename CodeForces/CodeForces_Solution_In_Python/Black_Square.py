#Black_Square
a,b,e,d=map(int,input().split())
s=input()
c=0
for i in s:
    if(i=='1'):
        c+=a
    elif(i=='2'):
        c+=b
    elif(i=='3'):
        c+=e
    else:
        c+=d
print(c)        