#Snake_Procession
for _ in range(int(input())):
    n = int(input())
    a = input()
    s = ''
    for i in a:
        if i.isalpha() == True:
            s += i
    flag = True
    if len(s) % 2 != 0:
        flag = False
    else:
        for i in range(0,len(s)-1,2):
            if s[i] == 'H' and s[i+1] == 'T':
                flag = True
            else:
                flag = False
                break
    if flag:
        print("Valid")
    else:
        print("Invalid")