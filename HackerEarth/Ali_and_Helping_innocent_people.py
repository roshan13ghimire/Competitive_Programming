#Ali_and_Helping_innocent_people
s = input()
f1 = s[2] not in "AEIOUY"
f2 = (int(s[7])+int(s[8]))%2==0
f3 = (int(s[0])+int(s[1]))%2==0
f4 = (int(s[3])+int(s[4]))%2==0
f5 = (int(s[4])+int(s[5]))%2==0
if(f1 and f2 and f3 and f4 and f5):
    print('Valid')
else:
    print('Invalid')
