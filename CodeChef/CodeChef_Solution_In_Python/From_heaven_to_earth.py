#From_heaven_to_earth
import math
for _ in range(int(input())):
    s = math.sqrt(2)
    n , v1 , v2 = map(int,input().split())
    if s * v1 * n > v2 * n:
        print("Stairs")
    else:
        print("Elevator")