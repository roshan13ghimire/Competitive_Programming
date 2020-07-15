#Chef_and_his_Sequence
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    j = 0
    for i in range(n):
        if (a[i]==b[j]):
            j+=1
            if (j==m):
                break
    if (j==m):
        print("Yes")
    else:
        print("No")