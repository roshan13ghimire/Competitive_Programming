#tram
n=int(input())
c=0
mc=0
for i in range(n):
    a,b=map(int,input().split())
    c+=(b-a)
    mc=max(mc,c)
print(mc)    