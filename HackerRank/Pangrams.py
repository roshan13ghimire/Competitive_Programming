#Pangrams
from collections import Counter
s=input()
a=s.lower()
if(len(s)<26):
    print("not pangram")
    exit()
if(len(Counter(s.lower()))==26):
    print("not pangram")
else:
    print("pangram")