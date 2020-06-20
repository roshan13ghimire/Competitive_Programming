#The_Lead_Game
t=int(input())
l=[]
s=[]
c=0
d=0
for i in range(t):
    a,b=map(int,input().split())
    c+=a
    d+=b
    if(a>b):
        l.append(c-d)
    else:
        s.append(d-c)
        
#print(l)
#print(s)
if(max(l)>max(s)):
    print(1,max(l))
else:
    print(2,max(s))