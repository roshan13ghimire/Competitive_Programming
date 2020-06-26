#Funny_String
for _ in range(int(input())):
    s=input()
    t=s[::-1]
    l=[]
    k=[]
    for i in range(1,len(s)):
        l.append(abs(ord(s[i-1])-ord(s[i])))
        k.append(abs(ord(t[i-1])-ord(t[i])))
    #print(l)
    #print(k)
    if(k==l):
        print("Funny")
    else:
        print("Not Funny")
        