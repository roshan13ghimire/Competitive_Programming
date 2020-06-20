#queue_at_the_school
n,t=map(int,input().split())
s=input()
nl=list(s)
for _ in range(t):
    #print(l)
    l=[]
    for j in range(len(l)):
        l.append(nl[j])
    i=1
    while(i<len(l)):
       # print(i)
        if(l[i-1]=='B' and l[i]=='G'):
            l[i-1],l[i]=l[i],l[i-1]
            i+=1
            print("".join(l))
        i+=1
        nl=l
        