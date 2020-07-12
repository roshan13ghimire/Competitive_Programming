#Forgotten_Language
for _ in range(int(input())):
    n,k=map(int,input().split())
    b=''
    p=[]
    a=list(map(str,input().split()))
    for _ in range(k):
        l=list(map(str,input().split()))
        for i in range(1,len(l)):
            p.append(l[i])
    for i in range(len(a)):
        if(a[i] in p):
            b+='YES '
        else:
            b+='NO '
    print(b)            