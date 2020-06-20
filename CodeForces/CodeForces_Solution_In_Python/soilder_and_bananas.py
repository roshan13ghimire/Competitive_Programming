#soilder_and_bananas
k,n,w=map(int,input().split())
a=k*(w*(w+1)/2)
if(a<n):
    print("0")
else:
    print(int(a-n))
    