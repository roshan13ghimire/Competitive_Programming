#Anton_and_Letters
s=input()
l=[]
for i in s:
    if(i>='a' and i<='z'):
        l.append(i)
print(len(set(l)))        