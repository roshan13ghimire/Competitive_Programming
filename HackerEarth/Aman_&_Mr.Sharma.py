#Aman_&_Mr.Sharma
c = 0
for _ in range(int(input())):
    r , x = map(int,input().split())
    if int(22/7 * 2 * r) <= 100 * x:
        c+= 1
print(c)