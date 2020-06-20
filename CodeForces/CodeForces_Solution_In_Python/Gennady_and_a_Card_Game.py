#Gennady_and_a_Card_Game
s=input()
a=list(map(str,input().split()))
for i in a:
    if(s[:1]==i[:1] or s[1:]==i[1:]):
        print("YES")
        exit()
    else:
        continue
print("NO")