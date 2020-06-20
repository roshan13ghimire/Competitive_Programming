#Second_Largest 
t=int(input())
for i in range(t):
    l=[]
    a,b,c=map(int,input().split())
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    print(l[1])