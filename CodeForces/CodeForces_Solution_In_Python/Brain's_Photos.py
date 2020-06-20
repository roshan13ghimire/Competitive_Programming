#Brain's_Photos
n,m=map(int,input().split())
p=0
for i in range(n):
    l=list(map(str,input().split()))
    for i in range(len(l)):
        if(l[i]=='C' or l[i]=='M' or l[i]=='Y'):
            p+=1
if(p>=1):
    print("#Color")
else:
    print("#Black&White")