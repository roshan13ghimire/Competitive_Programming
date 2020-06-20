#Total_Expenses
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a<1000):
        print("{:.6f}".format(a*b))
    else:
        print("{:.6f}".format(a*b-(10/100)*(a*b)))
        