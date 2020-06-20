#word
s=input()
c=0
d=0
for i in s:
    if(i.isupper()==True):
        c+=1
    elif(i.islower()==True):
        d+=1
if(c>d):
    print(s.upper())
else:
    print(s.lower())