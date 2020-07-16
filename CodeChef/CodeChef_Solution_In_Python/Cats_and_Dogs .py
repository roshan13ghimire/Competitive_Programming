#Cats_and_Dogs 
for _ in range(int(input())):
    c, d, l = map(int, input().split())
    if l % 4 != 0 or d*4 > l:
        print('no')
    else:
        lr = l-d*4
        if c*4 < lr:
            print('no')
        else:
            c = c-lr/4
            if c > 2*d:
                print('no')
            else:
                print('yes')

        
        