#Police_Recruits
n=int(input())
a=list(map(int,input().split()))
c=0
o=0
for i in range(len(a)):
    if(a[i]<0):
        if(not (o>=1)):
            c+=1
        else:
            o-=1
    else:
        o+=a[i]
print(c)        