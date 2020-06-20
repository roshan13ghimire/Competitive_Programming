#drinks
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    c+=float(a[i]/100)
s=float(c/len(a))*100    
print("{:.12f}".format(s))    