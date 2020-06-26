#Gemstones
n=int(input())
l=[]
for _ in range(n):
    s=input()
    l.append(set(s))
for i in range(1,len(l)):
    a=l[i-1] & l[i]
    l[i]=a
print(len(a))