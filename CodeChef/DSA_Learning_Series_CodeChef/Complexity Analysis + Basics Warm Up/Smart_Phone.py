#Smart_Phone
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()
c=0
for i in range(n):
    if(l[i]*(n-i)>c):
        c=l[i]*(n-i)
print(c)       