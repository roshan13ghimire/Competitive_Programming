#Chef_and_String
s = input()
a = 0 
b = 0
c = 0
d = 0
for i in range(len(s)):
    if s[i]=='C':
        a+=1
    elif s[i]=='H' and b<a:
        b+=1
    elif s[i]=='E' and c<b:
        c+=1
    elif s[i]=='F' and d<c:
        d+=1
    else:
        continue
print(d)