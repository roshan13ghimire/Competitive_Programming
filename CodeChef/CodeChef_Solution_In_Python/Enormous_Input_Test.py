#Enormous_Input_Test
n,k=map(int,input().split())
c=0
for i in range(n):
    a=int(input())
    if(a%k==0):
        c+=1
print(c)       