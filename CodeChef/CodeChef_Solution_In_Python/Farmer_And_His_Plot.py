#Farmer_And_His_Plot
for _ in range(int(input())):
    l,b=map(int,input().split())
    num=1
    for i in range(2,max(l, b)):
        if(l%i==0 and b%i==0):
            num=i
    print((l//num)*(b//num))