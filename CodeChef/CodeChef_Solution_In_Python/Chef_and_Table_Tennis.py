#Chef_and_Table_Tennis
for _ in range(int(input())):
    s = input()
    if s.count('1') < s.count('0'):
        print("LOSE")
    else:
        print("WIN")