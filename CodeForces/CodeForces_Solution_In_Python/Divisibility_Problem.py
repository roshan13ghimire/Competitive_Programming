#Divisibility_Problem
t=int(input())
for i in range(t):
    c=0
    a,b=map(int,input().split())
    if(a%b==0):
        print(0)
    else:
        print(b-(a%b))