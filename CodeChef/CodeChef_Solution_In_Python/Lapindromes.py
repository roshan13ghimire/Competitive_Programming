#Lapindromes 
from collections import Counter
for _ in range(int(input())):
    s=input()
    if(len(s)%2==0):
        if(Counter(s[:len(s)//2])==Counter(s[len(s)//2:])):
            print("YES")
        else:
            print("NO")
    else:
        if(Counter(s[:len(s)//2])==Counter(s[(len(s)//2)+1:])):
            print("YES")
        else:
            print("NO")
    #print(s[len(s)//2+1:])
    #print(s[:len(s)//2])