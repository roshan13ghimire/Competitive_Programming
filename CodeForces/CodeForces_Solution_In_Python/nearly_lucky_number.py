# nearly_lucky_number
n=input()
l=list(n)
a=l.count('4')
b=l.count('7')
if(a+b==4 or a+b==7):
    print("YES")
else:
    print("NO")