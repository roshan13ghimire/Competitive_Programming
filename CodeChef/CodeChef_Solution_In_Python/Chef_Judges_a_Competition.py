#Chef_Judges_a_Competition
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    amax = max(a)
    bmax = max(b)
    if sum(a) - amax > sum(b) - bmax:
        print("Bob")
    elif sum(a) - amax < sum(b) - bmax:
        print("Alice")
    else:
        print("Draw")