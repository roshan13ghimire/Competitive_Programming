#Temple_Land
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = list(range(1,n//2+2))
    l = []
    print(s)
    for i in range(len(s)-1):
        b = a.count(s[i])
        l.append(b)
    print(l)
    if list(set(a)) == s and len(set(l)) == 1:
        print("yes")
    else:
        print("no")