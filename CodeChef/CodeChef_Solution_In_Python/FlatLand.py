#FlatLand
import math
for _ in range(int(input())):
    n = int(input())
    d = 0
    while n!= 0:
        c = int(math.sqrt(n))
        n-= c * c
        d+= 1
    print(d)