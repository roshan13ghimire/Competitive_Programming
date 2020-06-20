#Gross_Salary
for _  in range(int(input())):
    bs=int(input())
    if(bs<1500):
        gs=bs+(10/100)*bs+(90/100)*bs
    else:
        gs=bs+500+(98/100)*bs
    print("{:.2f}".format(gs))    