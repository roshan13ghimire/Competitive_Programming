#Alternating_Characters
for _ in range(int(input())):
    s=input()
    d=0
    for i in range(1,len(s)):
        if(s[i-1]==s[i]):
            d+=1
    print(d)        
