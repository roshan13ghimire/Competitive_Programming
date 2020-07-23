#Database
T=int(input())
for a in range(T):
    length=list(map(int,input().split()))
    column_names=list(map(str,input().split()))
    L=[]
    dashedline='+'
    col='|'
    s1=[]
    for i in range(length[1]):
        L.append(list(map(str,input().split())))
    for i in range(length[0]):
        s=len(column_names[i])
        for j in range(length[1]):
            if len(L[j][i])>s:
                s=len(L[j][i])
        dashedline+='-'*(s+2)+'+'
        col+=' '+column_names[i]+' '*(s-len(column_names[i]))+' |'
        s1.append(s)
    print(dashedline)
    print(col)
    print(dashedline)
    for i in range(length[1]):
        rows='|'
        for j in range(length[0]):
            if L[i][j].isdigit():
                rows+=' '+' '*(s1[j]-len(L[i][j]))+L[i][j]+' |'
            else:
                rows+=' '+L[i][j]+' '*(s1[j]-len(L[i][j]))+' |'
        print(rows)
    print(dashedline)