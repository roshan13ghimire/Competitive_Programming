#Cipher
s = input()
d = s
k = int(input())
a = ''
for i in d:
    if i.isalpha() == True:
        if i.isupper() == True:
            a+= (chr((ord(i) + k - 65) % 26 + 65))
        elif i.islower() == True:
            a+= (chr((ord(i) + k - 97) % 26 + 97))
    elif  i.isdigit() == True:
        a+= (str((int(i) + k) % 10))
    else:
        a+= i
print(a)