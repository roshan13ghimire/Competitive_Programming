#Fox _And_Snake
r,c=map(int,input().split())
for i in range(1,r+1):
    for j in range(1,c+1):
        if(i%2!=0):
            print("#",end='')
        else:
            if(i%4==2 and j==c):
                print("#",end='')
            elif(i%4==0 and j==1):
                print("#",end='')
            else:
                print(".",end='')
                
    print('')