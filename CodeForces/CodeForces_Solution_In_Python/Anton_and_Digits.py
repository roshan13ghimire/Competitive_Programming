#Anton_and_Digits
a,b,c,d=map(int,input().split())
m=min(a,c,d)
a-=m
n=min(a,b)
print(m*256+n*32)