#Rectangle
for _ in range(int(input())):
    a=list(map(int,input().split()))
    a.sort()
    if(a[0]==a[1] and a[2]==a[3]):
        print("YES")
    else:
        print("NO")
    