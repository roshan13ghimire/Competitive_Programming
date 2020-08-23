#Distribute_Candies
for _ in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    if(len(a)==0):
        print(a[0])
    elif(len(a)==1):
        print(min(a))
    else:
        a.sort(reverse=True)
        s=0
        for i in range(2,len(a),3):
            s+=a[i]
        print(s)    
        
