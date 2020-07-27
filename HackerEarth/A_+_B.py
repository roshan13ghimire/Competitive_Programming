#A_+_B
while True:
    try:
        a , b = map(int,input().split())
        print(a + b)
    except EOFError:
        break