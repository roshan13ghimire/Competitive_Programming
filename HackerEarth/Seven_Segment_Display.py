#Seven_Segment_Display
a = [6,2,5,5,4,5,6,3,7,6]
for _ in range(int(input())):
    n = [i for i in input()]
    for i in range(len(n)):
        n[i] = int(n[i])
    s = 0
    for i in range(len(n)):
         s+= a[n[i]]
    c = s // 2
    if s % 2 == 0:
        ans = '1' * c
    else:
        ans = '7' + '1'* (c - 1)
    print(ans)