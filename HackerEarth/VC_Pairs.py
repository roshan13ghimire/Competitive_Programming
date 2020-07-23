#VC_Pairs
def consonant(i):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        return False
    else:
        return True
for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    for i in range(n-1):
        d = consonant(s[i])
        if (d == True and s[i+1] == 'a') or (d == True and s[i+1] == 'e') or (d == True and s[i+1] == 'i') or (d == True and s[i+1] == 'o') or (d == True and s[i+1] == 'u'):
            c+= 1
    print(c)