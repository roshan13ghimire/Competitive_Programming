#Bear_and_Candies_123
for _ in range(int(input())):
    a,b = map(int,input().split())
    x,y = 1,2
    while(True):
        if(a>=x):
            a = a - x
            x = x + 2
        else:
            print("Bob")
            break
        if(b>=y):
            b = b - y
            y = y + 2
        else:
            print("Limak")
            break