#I_love_%username%
n=int(input())
a=list(map(int,input().split()))
c=0
p=q=a[0]
for i in range(len(a)):
    if(p>a[i]):
        c+=1
        p=a[i]
    if(q<a[i]):
        c+=1
        q=a[i]
print(c)        
        