#Mishka_and_Game
n=int(input())
m,c=0,0
while(n!=0):
    a,b=map(int,input().split())
    if(a>b):
        m+=1
    if(a<b):
        c+=1
    n-=1        
if(m>c):
    print("Mishka")
elif(m==c):
    print("Friendship is magic!^^")
else:
    print("Chris")