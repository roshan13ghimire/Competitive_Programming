#Bricks_Game
n = int(input())
i = 1
while(True):
    if n <= i:
        print("Patlu")
        break
    n-= i
    if n <= i * 2:
        print("Motu")
        break
    n-= i*2
    i+= 1
    
    
    
    