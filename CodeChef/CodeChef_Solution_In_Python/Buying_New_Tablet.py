#Buying_New_Tablet
for _ in range(int(input())):
    n , b = map(int,input().split())
    c = 0
    for _ in range(n):
        w , h , p = map(int,input().split())
        if p <= b:
            d = w * h
            if d > c:
                c=d
    if c == 0:
        print("no tablet")
    else:
        print(c)