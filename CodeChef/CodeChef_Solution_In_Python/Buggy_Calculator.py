#Buggy_Calculator
for _ in range(int(input())):
    a , b = map(int,input().split())
    c , s , d = 0 , 0 , 1
    while a > 0 or b > 0:
        c = (int(a%10) + int(b%10)) % 10
        s += c * d 
        d *=10
        a /=10 
        b /=10
    print(int(s))