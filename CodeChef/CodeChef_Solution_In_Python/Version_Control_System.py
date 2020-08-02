#Version_Control_System
for _ in range(int(input())):
    n , m , k = map(int,input().split())
    tf = list(range(1 , n+1))
    i = list(map(int,input().split()))
    t = list(map(int,input().split()))
    a = 0
    b = 0
    for f in tf:
        if f in i and f in t:
            a += 1
        elif f not in i and f not in t:
            b += 1
    print(a , b)
