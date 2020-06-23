#Patrick_and_Shopping
a,b,c=map(int,input().split())
print(min(a+b+c,2*(a+b),2*(b+c),2*(c+a)))