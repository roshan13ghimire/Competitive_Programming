#Split_houses
n = int(input())
s = input()
a = ''
flag = True
for i in s:
    if('HH' in s):
        print('NO')
        flag = False
        break
    elif(i =='.'):
        a+= 'B'
    else:
        a+= i
if(flag):
    print('YES')
    print(a)

