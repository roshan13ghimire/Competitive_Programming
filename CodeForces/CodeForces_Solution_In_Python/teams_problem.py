#teams_problem
n=int(input())
count=0
for _ in range(n):
    a=list(map(int,input().split()))
    c=len(list(filter(lambda x: x>0 , a)))
    if(c==0 or c==1):
        continue
    else:
        count+=1
print(count)        
        
        
        