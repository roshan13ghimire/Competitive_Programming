#Chef_and_Dolls
for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        d=int(input())
        if d in l:
            l.remove(d)
        else:
            l.append(d)
    print(l[0])        

            
