#Brackets
for _ in range(int(input())):
    s = input()
    b = 0
    mb = 0
    for i in range(len(s)):
        if s[i] == '(':
            b += 1
        else:
            b -= 1
        mb = max(mb, b)
        
    b = '(' * mb + ')' * mb
    print(b)
        