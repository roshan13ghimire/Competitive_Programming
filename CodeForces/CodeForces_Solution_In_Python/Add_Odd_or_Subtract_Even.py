#Add_Odd_or_Subtract_Even
for i in range(int(input()):
    a,b=map(int,input().split())
    if(b>a):
        if((b-a)%2!=0):
            print(1)
        else:
            print(2)
    elif(a==b):
        print(0)
    else:
        if((a-b)%2!=0):
            print(2)
        else:
            print(1)            
