#Chef_and_his_Students
for _ in range(int(input())):
    s = input()
    c = 0
    for i in range(len(s)-1):
        if s[i] == '<'  and s[i+1] == '>':
            c+= 1
    print(c)