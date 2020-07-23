#Duration
for _ in range(int(input())):
    sh , sm , eh , em = map(int,input().split())
    if em < sm:
        print(eh - sh -1 , 60 - abs(sm - em))
    else:
        print(eh - sh  ,  abs(em - sm))