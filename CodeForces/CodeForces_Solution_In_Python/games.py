#games
n=int(input())
s=[]
l=[]
c=0
for i in range(n):
    a,b=map(int,input().split())
    l.append(a)
    s.append(b)
for i in range(len(l)):
    for j in range(len(s)):
        if(l[i]==s[j]):
            c+=1
print(c)            