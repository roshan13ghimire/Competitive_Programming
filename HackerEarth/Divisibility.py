#Divisibility
n = int(input())
a = list(map(int,input().split()))
c = 0
d = ''
for i in a:
    c = i % 10
    d+= str(c)
if int(d) % 10 == 0:
    print("Yes")
else:
    print("No")