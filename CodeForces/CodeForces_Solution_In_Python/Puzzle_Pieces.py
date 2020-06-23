#Puzzle_Pieces
for _ in range(int(input())):
    m,n=map(int,input().split())
    if(m==1 or n==1 or(n==m and n==2)):
        print("YES")
    else:
        print("NO")
