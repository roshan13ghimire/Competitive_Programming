#presents
n=int(input())
a=list(map(int,input().split())) #2 3 4 1
l=[0]*n
for i in range(len(a)):
    l[a[i]-1]=i+1
for i in range(len(l)):
    print(l[i],end=' ')