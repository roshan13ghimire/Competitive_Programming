#Soft_Drinking
n,k,l,c,d,p,a,b=map(int,input().split())
print(min(k*l//a,c*d,p//b)//n)