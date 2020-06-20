#next_round_roblem
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
if(a[k-1]==0):
    count= len(list(filter(lambda x: (x > 0), a)))
    if(count<=0):
        print(0)
        exit()
    else:
        print(count)
        exit()
for i in range(len(a)):
    if(a[i]>=a[k-1]):
        c+=1
print(c)        
