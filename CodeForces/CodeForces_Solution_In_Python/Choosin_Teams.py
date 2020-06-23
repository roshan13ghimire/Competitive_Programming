#Choosin_Teams
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i<=5-k:
        c+=1
print(c//3)