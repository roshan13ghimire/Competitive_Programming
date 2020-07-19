#Tickets
for _ in range(int(input())):
    s = input()
    if len(set(s)) == 2:
        print("YES")
    else:
        print("NO")