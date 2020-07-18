#Devu_and_Grapes
for _ in range(int(input())):
    n ,k = map(int,input().split())
    a = list(map(int,input().split()))
    c = 0
    for i in a:
        p = i % k
        q = k - p
        if i >= k: 
            c = c + min(p,q)
        else:
            c = c + q
    print(c)