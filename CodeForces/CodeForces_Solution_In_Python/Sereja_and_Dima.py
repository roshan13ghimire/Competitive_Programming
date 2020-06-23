#Sereja_and_Dima
n=int(input())
a=list(map(int,input().split()))
x,y=0,0
for i in range(n):
    k=max(a[0],a[-1])
    if i%2==0:
        x+=k
    else: 
        y+=k
    a.remove(k)
print(x,y)