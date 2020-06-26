#MarsExploration
s=input()
c=0
for i in range(len(s)):
    if(s[i]!='SOS'[i%3]):
        c+=1
print(c)        