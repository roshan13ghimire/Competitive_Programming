#Chef_and_Gift
for _ in range(int(input())):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    l = len([a[i] for i in range(n) if a[i] % 2 == 0])   
    if k == 0 and l == n:
        print("NO")
    elif l >= k:
        print("YES")
    else:
        print("NO")