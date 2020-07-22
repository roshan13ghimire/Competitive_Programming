#Toggle_String
s = input()
c = ''
for i in s:
    if i.isupper() ==  True:
        c+= i.lower()
    else:
        c+= i.upper()
print(c)
        