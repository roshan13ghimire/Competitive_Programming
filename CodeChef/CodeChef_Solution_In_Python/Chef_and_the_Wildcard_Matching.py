#Chef_and_the_Wildcard_Matching
for _ in range(int(input())):
    s=input()
    t=input()
    c=1
    for i in range(len(s)):
        if(s[i]==t[i]):
             continue
        elif(s[i]=='?'):
            continue
        elif(t[i]=='?'):
            continue
        else:
            c=0
            break
    if(c==0):
        print("No")
    else:
        print("Yes")