#panagram
n=int(input())
s=input()
l=''
for i in s:
    if(i.isupper()==True):
        l+=i.lower()
    else:
        l+=i        
if(len(set(l))==26):
    print("YES")
else:
    print("NO")