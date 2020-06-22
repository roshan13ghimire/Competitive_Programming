#Greedy_puppy
for _ in range(int(input())):
    n,k=map(int,input().split())
    d=0
    for i in range(2,k+1):
        if(d<n%i):
            d=n%i
    print(d)    