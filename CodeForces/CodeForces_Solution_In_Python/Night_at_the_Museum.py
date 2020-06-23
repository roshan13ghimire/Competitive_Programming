#Night_at_the_Museum
s=input()
ans=0
i='a'
for c in s:
    l=abs(ord(c)-ord(i))
    ans=ans+min(l,26-l)
    i=c
print(ans)
 