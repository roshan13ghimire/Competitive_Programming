#Modified_Kaprekar_Numbers
p=int(input())
q=int(input())
l=[]
if(p==1):
    l.append(p)
for i in range(p,q+1):
    c=str(i*i)
    a=c[:len(c)//2]
    b=c[len(c)//2:]
    if(len(a)!=0):
        if(int(a)+int(b)==i):
            l.append(str(i))
if(len(l)!=0):
    print(' '.join([str(i) for i in l]))
else:
    print("INVALID RANGE")
    
    
