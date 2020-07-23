#IT’S_MAGIC!
n = int(input())
a = list(map(int,input().split()))
l = []
s = sum(a)
for  i in range(n):
    if (s - a[i]) % 7 == 0:
        l.append(a[i])
if len(l) != 0:
    print(a.index(min(l)))
else:
    print('-1')
    