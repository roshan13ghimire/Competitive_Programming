#Chef_and_String
for _ in range(int(input())):
    l=input()
    c=0
    i=1
    while(i<len(l)):
        if(abs(ord(l[i-1])-ord(l[i]))==1):
            c+=1
            i+=1
        i+=1
    print(c)