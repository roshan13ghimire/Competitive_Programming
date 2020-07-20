#Simple_Statistics
for _ in range(int(input())):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print("{:6f}".format(sum(a[k:len(a)-k])/len(a[k:len(a)-k])))