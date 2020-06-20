#i_wanna_be_the_guy
n=int(input())
l=[]
m=[]
xi=list(map(int,input().split()))
yi=list(map(int,input().split()))
for i in range(1,len(xi)):
    l.append(xi[i])
for i in range(1,len(yi)):
    l.append(yi[i])
m=set(l)
a=range(1,n+1)
if(len(m)==len(a)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")