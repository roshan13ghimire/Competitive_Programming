#Easy_Math
for _ in range(int(input())):
    l = []
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            su = 0
            p = a[i] * a[j]
            for z in str(p):
                su += int(z)
            l.append(su)
    print(max(l))
