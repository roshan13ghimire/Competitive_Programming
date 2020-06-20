#ulta_fast_mathematician
n=input()   #1010100
k=input()   #0100101
s=''         
for i in range(len(n)):
    for j in range(i,len(k)):
        if(n[i]==k[j]):
            s+='0'
            break
        else:
            s+='1'
            break
print(s)            