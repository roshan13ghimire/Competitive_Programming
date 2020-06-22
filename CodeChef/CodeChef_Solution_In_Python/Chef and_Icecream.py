#Chef and_Icecream
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    d=0
    e=0
    fl=True
    if(a[0]>5):
        print("NO")
    else:
        for i in range(len(a)):
            if(a[i]==5):
                c+=1
            elif(a[i]==10):
                d+=1
                c-=1
            else:
                if(d>0):
                    d-=1
                else:
                    c-=2
            if(c<0 or d<0):
                fl=False
                break
        if(fl==True):
            print("YES")
        else:
            print("NO")
            
        