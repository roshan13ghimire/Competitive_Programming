#Sum_of_Digits 
t=int(input())
for i in range(t):
    n=int(input())
    s=0
    while(n!=0):
        d=n%10
        s+=d
        n//=10
    print(s)    