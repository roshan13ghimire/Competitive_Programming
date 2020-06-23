#Honest_Coach
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    l=[]
    for i in range(1,n):
        l.append(abs(a[i-1]-a[i]))
    print(min(l))    