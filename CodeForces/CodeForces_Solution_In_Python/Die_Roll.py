#Die_Roll
y,w=map(int,input().split())
d=max(y, w)
s=['1/1', '5/6', '2/3', '1/2', '1/3', '1/6']
print(s[d-1])