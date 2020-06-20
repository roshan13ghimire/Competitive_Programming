#Tanu_and_Head-bob
for _ in range(int(input())):
    n=int(input())
    s=input()
    if('I' in s):
        print('INDIAN')
    elif(('Y' in s) or(('Y' in s) and ('N' in s) and ('I' not in s))):
        print('NOT INDIAN')
    else:
        print("NOT SURE")