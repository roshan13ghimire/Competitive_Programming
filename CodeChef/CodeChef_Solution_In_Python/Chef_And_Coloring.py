#Chef_And_Coloring
for _  in range(int(input())):
    n = int(input())
    s = input()
    r,g,b=0,0,0
    for i in s:
        if (i=='R'):
            r+=1
        elif (i=='G'):
            g+=1
        elif (i=='B'):
            b+=1
    print(min(r+b,b+g,g+r))