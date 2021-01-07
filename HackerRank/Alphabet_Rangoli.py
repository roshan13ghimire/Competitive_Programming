#Alphabet_Ragoli
def rangoli(size):
    myStr = "abcdefghijklmnopqrstuvwxyz"[0:size]
    for i in range(size-1,-size,-1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1]+myStr[x:size]
            print ("--"*x+ '-'.join(line)+"--"*x)

if __name__ == '__main__':
    n = int(input())
    rangoli(n)
