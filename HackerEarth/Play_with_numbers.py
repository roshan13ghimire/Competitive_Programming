#Play_with_numbers
n , q = map(int,input().split())
a = list(map(int,input().split()))
b = [0] * n
b[0] = a[0]
for i in range(1,len(a)):
    b[i] = b[i - 1] + a[i]
for i in range(q):
    l , r = map(int,input().split())
    if l == 1:
        print(b[r-1] // ((r - l) + 1))
    else:
        print((b[r-1] - b[l-2]) // ((r - l) + 1))
