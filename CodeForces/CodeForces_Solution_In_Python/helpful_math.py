#helpful_math
a=input()
l=[]
if(len(a)==1):
    print(a)
    exit()
else:
    for i in a:
        if(i.isdigit()==True):
            l.append(int(i))
c=sorted(l)
for i in range(len(l)-1):
    print(str(c[i])+'+',end='')
print(c[len(c)-1])    


        