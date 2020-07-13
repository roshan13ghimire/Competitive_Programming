#Chef_and_Rainbow_Array
l={1,2,3,4,5,6,7}
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(a==a[::-1] and set(a)==l):
        print("yes")
    else:
        print("no")