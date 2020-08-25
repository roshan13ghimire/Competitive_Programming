#Nested_Lists
d = {}
for _ in range(int(input())):
    s = input()
    n = float(input())
    d[s] = n
v = d.values()
l = sorted(list(set(v)))[1]
k = []
for key,value in d.items():
    if value == l:
        k.append(key)
k.sort()
for i in k:
    print(i)