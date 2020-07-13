#Chef_and_digits_of_a_number
for _ in range(int(input())):
    s=input()
    on=0
    ze=0
    for i in s:
        if(i=='1'):
            on+=1
        else:
            ze+=1
    if(on==1 or ze==1):
        print('Yes')
    else:
        print('No')