#Even_Array
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    z,o=0,0
    for i in range(n):
        if(i%2!=l[i]%2):
            if(i%2==0):
                z+=1
            else:
                o+=1
    if(z==o):
        print(z)
    else:
        print("-1")