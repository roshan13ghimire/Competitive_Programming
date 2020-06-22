#Chef_and_Two_Strings
for _ in range(int(input())):
    s=input()
    t=input()
    m=len(s)
    mi=0
    for i in range(len(s)):
        if(s[i]==t[i] and s[i]!='?'):
            m-=1
        elif(s[i]!=t[i] and s[i]!='?' and t[i]!='?'):
            mi+=1
    print(mi,m)         
        