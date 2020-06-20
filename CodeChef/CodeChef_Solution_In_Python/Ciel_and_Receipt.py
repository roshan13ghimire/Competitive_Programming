#Ciel_and_Receipt 
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    p=[]
    s=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    while(n>0):
        for i in range(11,-1,-1):
            if(s[i]<=n):
                n-=s[i]
                #print(n)
                c+=1
                break
        p.append(c)
    print(len(p))