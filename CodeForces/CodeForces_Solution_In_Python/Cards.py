#Cards
n=int(input())
s=input()
a=s.count('z')
b=s.count('n')
for i in range(1,b+1):
    print(1,end=' ')
for i in range(1,a+1):
    print(0,end=' ')