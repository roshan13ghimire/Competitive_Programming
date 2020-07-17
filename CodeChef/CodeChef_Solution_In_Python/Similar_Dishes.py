#Similar_Dishes
for _ in range(int(input())):
    l = list(map(str,input().split()))
    s = list(map(str,input().split()))
    c = 0
    for i in range(len(s)):
        if s[i] in l:
            c+= 1
    if c >= 2:
        print("similar")
    else:
        print("dissimilar")