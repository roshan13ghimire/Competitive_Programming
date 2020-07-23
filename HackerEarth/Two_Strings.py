#Two_Strings
import collections
for _ in range(int(input())):
    s , t = map(str,input().split())
    if collections.Counter(s) == collections.Counter(t):
        print("Yes")
    else:
        print("No")
