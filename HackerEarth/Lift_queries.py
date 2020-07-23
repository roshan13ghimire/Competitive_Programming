#Lift_queries 
la = 0 
lb = 7 
for _ in range(int(input())):
    n = int(input())
    if n - la <= lb - n:
        print("A")
        la = n
    else:
        print("B")
        lb = n