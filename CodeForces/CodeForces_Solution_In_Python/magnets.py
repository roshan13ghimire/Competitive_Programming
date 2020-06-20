#magnets
n=int(input())
s=''
c=0
for i in range(n):
    a=input()
    s+=a
for i in range(1,len(s)):
    if(s[i-1]==s[i]):
        c+=1
print(c+1)        