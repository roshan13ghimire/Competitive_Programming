#The_Smallest_Pair
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print(a[0]+a[1])