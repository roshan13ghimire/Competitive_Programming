#Holiday_Of_Equality
n=int(input())
a=list(map(int,input().split()))
d=0
if(n==1):
    print(0)
    exit()
m=max(a)
for i in range(len(a)):
    c=m-a[i]
    d+=c
print(d)