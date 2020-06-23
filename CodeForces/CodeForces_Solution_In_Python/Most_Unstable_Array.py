#Most_Unstable_Array
for i in range(int(input())):
    n , k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    b.reverse()
    for x in range(k):
        if a[x]<b[x]:
            a[x],b[x]=b[x],a[x]
    print(sum(a))