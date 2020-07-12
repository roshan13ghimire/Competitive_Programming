#Two_vs_Ten
for _ in range(int(input())):
    n=int(input())
    if(n%10==0):
        print("0")
    elif((n*2)%10==0):
        print("1")
    else:
        print("-1")