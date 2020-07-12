#Piece_of_cake
for _ in range(int(input())):
    s=list(input())
    d=len(s)
    f=0
    for i in s:
        if(s.count(i)==d/2):
            f=1
            break
    if(f==1):
        print("YES")
    else:
        print("NO")
        
    
