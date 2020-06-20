#Vasya_the_Hipster
a,b=map(int,input().split())
if(a<b):
    print(a%b,end=' ')
elif(a>b):
    print(b%a,end=' ')
else:
    print(a,end=' ')
print(abs(a-b)//2)    
    