#Chef_and_Fruits
for _ in range(int(input())):
    n , m , k = map(int,input().split())
    while k:
        if n == m:
            break
        else:
            if n < m:
                k -= 1
                n += 1
            else:
                k -= 1
                m += 1
    print(abs(n - m))
    
    