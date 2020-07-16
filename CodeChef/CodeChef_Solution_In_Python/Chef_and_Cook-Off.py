#Chef_and_Cook-Off
for _ in range(int(input())):
    a = list(map(int,input().split()))
    n = a.count(1)
    if n==0:
        print("Beginner")
    elif n==1:
        print("Junior Developer")
    elif n==2:
        print("Middle Developer")
    elif n==3:
        print("Senior Developer")
    elif n==4:
        print("Hacker")
    else:
        print("Jeff Dean")