#Balanced_Array
for i in range(int(input())):
    n=int(input())
    if(n%4!=0):
        print('NO')
    else:    
        print('YES')
        m=n//2
        sumeven=m*(m+1)
        i=1
        sumodd=1
        l=[1]
        l1=[]
        for k in range(2,n+1,2):
            l1.append(k)
        #print(l1)
        while(sumeven!=sumodd):
            i=i+2 # 1 3
            sumodd=sumodd+i # 1 4 9 16 25 36 
            if(sumodd<sumeven):
                l.append(i)
                # 1 3 5 7
            elif(sumodd>sumeven):
                l.pop()
                sumodd -= (i-2)
                #print(sumodd,i)
                # 1 3 5 9
                l.append(i) # 1 3 5 11
            else:
                #l.pop() # 1 3 5 11
                l.append(i)
                break
            
        l3=l1+l
        #print(l)
        print(*l3,sep=' ')
        