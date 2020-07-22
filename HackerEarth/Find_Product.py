#Find_Product
n = int(input())
l = list(map(int,input().split()))
s = 1
for i in range(len(l)):
    s= (s * l[i]) % (10 ** 9 + 7)
print(s)