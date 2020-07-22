#Train_Partner
for _ in range(int(input())):
    n = int(input())
    if n % 8 == 1:
        print(str(n + 3) + "LB")
    if n % 8 == 2:
        print(str(n + 3) + "MB")
    if n % 8 == 3:
        print(str(n + 3) + "UB")
    if n % 8 == 4:
        print(str(n - 3) + "LB")
    if n % 8 == 5:
        print(str(n - 3) + "MB")
    if n % 8 == 6:
        print(str(n - 3) + "UB")
    if n % 8 == 7:
        print(str(n + 1) + "SU")
    if n % 8 == 0:
        print(str(n - 1) + "SL")
    