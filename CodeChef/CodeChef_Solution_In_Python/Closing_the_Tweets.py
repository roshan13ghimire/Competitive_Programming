#Closing_the_Tweets
n , k = list(map(int, input().split()))
l = set()
ans = 0
for i in range(k):
    s = input()
    if s == 'CLOSEALL':
        l = set()
        ans = 0
    else:
        a = s[6: ]
        if a not in l:
            l.add(a)
            ans += 1 
        else:
            l.remove(a)
            ans -= 1 
    print(ans)