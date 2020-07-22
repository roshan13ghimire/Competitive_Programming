#Zoos
s = input()
o = s.count('o')
z = s.count('z')
if o % 2 == 0 and o >= 2 * z:
    print("Yes")
else:
    print("No")