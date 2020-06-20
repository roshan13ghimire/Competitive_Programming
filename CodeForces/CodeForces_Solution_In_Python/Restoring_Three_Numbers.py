#Restoring_Three_Numbers
a,b,c,d=map(int,input().split())
m=max(a,b,c,d)
if(m!=a):
    print(m-a,end=' ')
if(m!=b):
    print(m-b,end=' ')
if(m!=c):
    print(m-c,end=' ')    
if(m!=d):
    print(m-d,end=' ')    