#Equalize_Prices_Again
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(((sum(l)-1)//n)+1)