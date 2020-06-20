#Team_Olympiad
t=int(input())
a=list(map(int,input().split()))
p=a.count(1)
q=a.count(2)
r=a.count(3)
g=0
if(1 not in a or 2 not in a or 3 not in a):
    print(0)
    exit()
while(p!=0 and q!=0 and r!=0):
    g+=1
    p-=1
    q-=1
    r-=1
print(g)    
while(1 in a and 2 in a and 3 in a):
    b=a.index(1)
    print(b+1,end=' ')
    a[b]=0
    c=a.index(2)
    print(c+1,end=' ')
    a[c]=0
    d=a.index(3)
    print(d+1)
    a[d]=0
        
        
        
    