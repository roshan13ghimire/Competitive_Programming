#Buy_a_Shovel
k,r=map(int,(input().split()))
a=str(k)
if(k%10==0):
    print(1)
    exit()
for i in range(1,10):
    a=k*i
    #print(a)
    if(a%10==r or a%10==0):
        print(i)
        break