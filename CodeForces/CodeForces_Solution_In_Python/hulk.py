#hulk
n=int(input())
for i in range(1,n+1):
    pos=i%2
    if(pos==1):
        print("I hate",end=' ')
    elif(pos==0):
        print("I love",end=' ')
    if(i!=n):
        print("that",end=' ')
print("it")        