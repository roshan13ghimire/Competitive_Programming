#New_Year_and_Hurry
n,k=map(int,input().split())
c,s=0,0
a=240-k
for i in range(1,n+1):
    s+=5*i
    if(s<=a):
        c+=1
print(c)        