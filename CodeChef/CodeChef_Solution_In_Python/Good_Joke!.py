#Good_Joke!
for _ in range(int(input())):
    N=int(input())
    ans=1
    for i in range(N):
        x=input()

    for i in range(2,N+1):
        ans^=i
    print(ans)