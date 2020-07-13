#Kitchen_Timetable
for _ in range(int(input())):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if(a[0]>=b[0]):
        c+=1
    for i in range(1,len(a)):
        if(a[i]-a[i-1]>=b[i]):
            c+=1
    print(c)