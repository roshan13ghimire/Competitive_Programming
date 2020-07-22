#Seating_Arrangement
for _ in range(int(input())):
    n = int(input())
    j = n // 12
    if n // 12 == n / 12:
        i = n // 12 + j -1
    else:
        i = n // 12 + j + 1
    if n <= 6 * i:
        c = (6 * i - n) * 2 + 1 + n
    else:
        c = n - (n - 6 * i) * 2 + 1
    k = n % 12
    if k % 6 == 3 or k % 6 == 4:
        seat = 'AS'
    elif k % 6 == 0 or k % 6 == 1:
        seat = 'WS'
    else:
        seat = 'MS'
    print(c,end=' ')
    print(seat)