#beautiful_matrix
a=[]
for i in range(5):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(5):
    for j in range(5):
        if(a[i][j]==1):
            print(abs(2-i)+abs(2-j))
        else:
            pass

