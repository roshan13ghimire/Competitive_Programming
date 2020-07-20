#Play_Piano
for _ in range(int(input())):
    s = input()
    flag = False
    for i in range(0,len(s)-1,2):
        if (s[i] == 'A' and s[i+1] == 'B') or (s[i] == 'B' and s[i+1] == 'A'):
            flag = True
        else:
            print("no")
            flag = False
            break
    if flag:
        print("yes")