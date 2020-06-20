#The_Block_Game
t=int(input())
for i in range(t):
    n=input()
    if(n==n[::-1]):
        print("wins")
    else:
        print("loses")