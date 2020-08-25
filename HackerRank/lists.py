#lists
l = []
for _ in range(int(input())):
    s = input()
    d = ''
    if s[:6] == 'insert':
        for i in s[7:]:
            if i == ' ':
                break
            if i.isdigit() == True:
                d+= i
        ele = s[len(d)+8:]
        l.insert(int(d),int(ele))
    if s[:5] == 'print':
        print(l)
    if s[:6] == 'remove':
        for i in s[7:]:
            if i == ' ':
                break
            if i.isdigit() == True:
                d+= i
        l.remove(int(d))
    if s[:6] == 'append':
        for i in s[7:]:
            if i == ' ':
                break
            if i.isdigit() == True:
                d+= i
        l.append(int(d))
    if s[:4] == 'sort':
        l.sort()
    if s[:3] == 'pop':
        del l[-1]
    if s[:7] =='reverse':
        l = l[::-1]
        