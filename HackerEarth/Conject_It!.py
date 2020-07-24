#Conject_It!
for _ in range(int(input())):
    n = int(input())
    while True:
        if n % 2 == 0:
            n//= 2
        else:
            n = 3 * n + 1
        if n == 1:
            print("YES")
            break
        elif n <= 0:
            print("NO")
            break