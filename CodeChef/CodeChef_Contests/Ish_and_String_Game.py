#Ish_and_String_Game
for _ in range(int(input())):
    s=input()
    t=input()
    c=''
    for i in s:
        if(i not in t):
            c+=i
    if(c):
        print(c)
    else:
        print(" ")
            