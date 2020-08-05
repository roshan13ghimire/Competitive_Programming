#Chef_and_Employment_Test
for _ in range(int(input())):
    n , k = map(int,input().split())
    a = list(map(int,input().split())) 
    a = sorted(a)
    for i in range(1,k+1):
        a.append(a[-1] + i)
    d = (n+k+1) // 2
    print(a[d-1])
        
