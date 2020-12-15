#last_year_substring
for _ in range(int(input())):
    n = int(input())
    s = input()
    l = 4
    r = 0
    flag = False
    while(l>=0):
        if s[:l] + s[len(s)-r:] == '2020':
            flag = True
            break
        else:
            l -= 1
            r += 1
    if flag:
        print("YES")
    else:
        print("NO")
            
            