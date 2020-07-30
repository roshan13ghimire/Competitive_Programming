#Three_Way_Communications
from math import sqrt
for _ in range(int(input())):
    r = int(input())
    x1 , y1 = map(int,input().split())
    x2 , y2 = map(int,input().split())
    x3 , y3 = map(int,input().split())
    s = 0
    d1 = sqrt((x1-x2)**2+(y1-y2)**2)
    d2 = sqrt((x2-x3)**2+(y2-y3)**2)
    d3 = sqrt((x1-x3)**2+(y1-y3)**2)
    if d1 <= r:
        s += 1
    if d2 <= r:
        s += 1
    if d3 <= r:
        s += 1
    if s >= 2:
        print('yes')
    else:
        print('no')