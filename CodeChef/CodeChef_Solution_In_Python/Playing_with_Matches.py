#Playing_with_Matches
for _ in range(int(input())):
    a ,b = map(int,input().split())
    c = str(a+b)
    d = 0 
    d+= c.count('0')*6
    d+= c.count('1')*2
    d+= c.count('2')*5
    d+= c.count('3')*5
    d+= c.count('4')*4
    d+= c.count('5')*5
    d+= c.count('6')*6
    d+= c.count('7')*3
    d+= c.count('8')*7
    d+= c.count('9')*6
    print(d)
        
    