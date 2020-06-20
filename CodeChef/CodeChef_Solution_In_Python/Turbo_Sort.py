#Turbo_Sort
n=int(input())
a=[]
for i in range(n):
    l=int(input())
    a.append(l)
a.sort()
for i in range(len(a)):
    print(a[i])