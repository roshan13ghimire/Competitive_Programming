#george_and_communication
n=int(input())
c=0
for i in range(n):
    p,q=map(int,input().split())
    if(p<q and (q-p)>1):
        c+=1
    else:
        continue
print(c)        