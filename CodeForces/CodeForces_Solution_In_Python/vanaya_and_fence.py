#vanaya_and_fence
n,h=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    if(a[i]<=h):
        c+=1
    else:
        c+=2
print(c)        