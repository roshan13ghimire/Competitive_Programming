#Combination_Lock
n=int(input())
a=input()
b=input()
c=0
for i in range(n):
    k=int(a[i])-int(b[i])
    if(k<0):
        k=-k
    if(k>5):
        k=10-k
    c+=k   
print(c)            