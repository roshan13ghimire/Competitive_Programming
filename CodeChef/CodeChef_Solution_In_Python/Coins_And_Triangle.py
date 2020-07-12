#Coins_And_Triangle
for _ in range(int(input())):
    n=int(input())
    c=0
    i=1
    a=n
    while(a>0):
        a-=i
        i+=1
        c+=1
        if(a<i):
            break
    print(c)    