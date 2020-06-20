#Bit++
n=int(input())
x=0
while(n!=0):
    a=input()
    if(a=='X++' or a=='++X'):
        x+=1
    else:
        x-=1
    n-=1
print(x)    