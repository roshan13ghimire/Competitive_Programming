#Caesar_Cipher
n=int(input())
s=input()      #middle-Outz
k=int(input())
d = s
a = ''
for i in d:
    if i.isalpha() == True:
        if i.isupper() == True:
            a+= (chr((ord(i) + k - 65) % 26 + 65))
        elif i.islower() == True:
            a+= (chr((ord(i) + k - 97) % 26 + 97))
    else:
        a+= i
print(a)