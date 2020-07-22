#Cost_of_balloons
for _ in range(int(input())):
    g , p = map(int,input().split())
    n = int(input())
    l = []
    m = []
    for _ in range(n):
        o , z = map(int,input().split())
        l.append(o)
        m.append(z)
    a = l.count(1)
    b = m.count(1)
    if a > b :
        print(a * min(g,p) + b * max(g,p))
    else:
        print(a * max(g,p) + b * min(g,p))