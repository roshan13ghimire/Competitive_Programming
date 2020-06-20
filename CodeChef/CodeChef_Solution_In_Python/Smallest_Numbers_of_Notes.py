#Smallest_Numbers_of_Notes
t=int(input())
a=[1,2,5,10,50,100]
for i in range(t):
    n=int(input())
    c=0
    for i in range(len(a)-1,-1,-1):
        while(n>=a[i]):
            n-=a[i]
            #print(n)
            c+=1
    print(c)
