#Ambiguous_Permutations 
import sys
while(True):
    n=int(input())
    if(n==0):
        break
    else:
        a=list(map(int,input().split()))
        l=[0]*n
        for i in range(len(a)):
            l[a[i]-1]=i+1
        if(l==a):
            print("ambiguous")
        else:
            print("not ambiguous")
        