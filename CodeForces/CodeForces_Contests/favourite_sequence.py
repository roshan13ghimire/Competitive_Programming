#favourite_sequence
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(0,len(a)//2):
        print(a[i],end=" ")
        print(a[len(a)-i-1],end=" ")
    if len(a)%2 != 0:
        print(a[len(a)//2],end=" ")