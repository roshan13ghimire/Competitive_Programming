#way_too_long_problem
n=int(input())
for _ in range(n):
    s=input()
    if(len(s)<=10):
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[len(s)-1])