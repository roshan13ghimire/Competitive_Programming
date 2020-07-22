#Chef_and_Bored_Games
for _ in range(int(input())):
    n = int(input())
    c = 0
    while n > 0:
        c+= n*n
        n-= 2
    print(c)