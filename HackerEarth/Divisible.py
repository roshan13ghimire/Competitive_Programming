#Divisible
n = int(input())
a = list(map(int,input().split()))
l = a[:len(a)//2]
b = a[len(a)//2 :]
d = ''
f = ''
for i in l:
    c = str(i)
    d+= c[:1]
for j in b:
    e = str(j)
    f+= e[len(e)-1:]
if int(d + f) % 11 == 0:
    print("OUI")
else:
    print("NON")