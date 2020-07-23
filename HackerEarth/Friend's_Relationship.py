#Friend's_Relationship
for _ in range(int(input())):
    n = int(input())
    for i in range(1,n+1):
        print('*'* i + '#' * 2 * (n -  i) + '*' * i)