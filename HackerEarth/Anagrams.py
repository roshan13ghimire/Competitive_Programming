#Anagrams
from collections import Counter
for _ in range(int(input())):
    a = input()
    b = input()
    A = Counter(a)
    B = Counter(b)
    e = A & B
    d = e.values()
    g = sum(d)
    print(len(a)+len(b)-2*(g))
