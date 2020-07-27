#Vowel_Recognition
for _ in range(int(input())):
    s = input()
    c = 0
    for j in range(len(s)):
        if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u' or s[j]=='A' or s[j]=='E' or s[j]=='I' or s[j]=='O' or s[j]=='U':
            c+= ((len(s) - j) * (j + 1))
    print(c)
    