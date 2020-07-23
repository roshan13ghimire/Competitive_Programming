#Book_of_Potion_making
n = int(input())
s = 0
i = len(str(n))
while(n != 0):
    d = n % 10
    s+= d * i
    n = n // 10
    i-= 1
if s % 11 == 0:
    print("Legal ISBN")
else:
    print("Illegal ISBN")