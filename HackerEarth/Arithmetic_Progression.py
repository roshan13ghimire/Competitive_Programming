#Arithmetic_Progression
import math
for _ in range(int(input())):
    a , b , c = map(int,input().split())
    if (b - a) - (c - b) == 0:
        print(0)
    else:
        print(math.ceil(abs((b - a) - ( c - b)) / 2))
    
    