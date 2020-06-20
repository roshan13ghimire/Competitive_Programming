#Sums in a Triangle
t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    for i in range(n):
        a=list(map(int,input().split()))
        l.append(a)
    #print(l)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1,1):
            l[i][j]+=max(l[i+1][j],l[i+1][j+1])
            #print(l[i][j])
    print(l[0][0])       