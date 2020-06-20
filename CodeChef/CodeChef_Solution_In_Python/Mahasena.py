#Mahasena
n=int(input())
a=list(map(int,input().split()))
c,d=0,0
for i in range(len(a)):
    if(a[i]%2==0):
        c+=1
    else:
        d+=1
if(c>d):
    print("READY FOR BATTLE")
else:
    print("NOT READY")