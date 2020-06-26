#Equalize_the_Array
n=int(input())
a=list(map(int,input().split()))
maxx=0
for i in range(len(a)):
    c=a.count(a[i])
    if(c>maxx):
        maxx=c
print(n-maxx)        