#Palindromic_substrings
for _ in range(int(input())):
    a = input()
    b = input()
    flag = False
    for i in a:
        if a.count(i) >= 1 and b.count(i) >= 1:
            print("Yes")
            flag = True
            break
    if not flag:
        print("No")
    