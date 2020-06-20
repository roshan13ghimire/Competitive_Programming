#Bus_to_Udayland
n=int(input())
c=0
l=[]
for i in range(n):
    a=input()
    if(a[:2]=='OO' and c==0):
        a="++"+a[2:]
        c+=1
        l.append(a)
    elif(a[3:]=='OO' and c==0):
        a=a[:3]+"++"
        c+=1
        l.append(a)
    else:
        l.append(a)
if(c==1):
    print("YES")
    for i in range(len(l)):
        print(l[i])
else:
    print("NO")
        
        