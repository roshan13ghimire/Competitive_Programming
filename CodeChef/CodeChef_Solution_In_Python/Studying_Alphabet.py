#Studying_Alphabet
s=input()
for _ in range(int(input())):
    a=input()
    flag=True
    for i in a:
        if(i not in s):
            flag=False
            break
    if(flag):
        print("Yes")
    else:
        print("No")