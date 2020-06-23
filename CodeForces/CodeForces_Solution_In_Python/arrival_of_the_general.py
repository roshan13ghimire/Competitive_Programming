#arrival_of_the_general
n=int(input())
a=list(map(int, input().split()))
x=a.index(max(a))
a.remove(a[x])
a.reverse()
y=a.index(min(a))
print(x + y)
        
