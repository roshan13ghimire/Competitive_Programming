#new_year_friends
x,y,z=map(int,input().split())
l=[]
l.append(x)
l.append(y)
l.append(z)
l.sort()
a=abs(x-l[1])
b=abs(y-l[1])
c=abs(z-l[1])
print(a+b+c)