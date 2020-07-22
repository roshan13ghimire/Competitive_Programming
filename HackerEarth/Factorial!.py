#Factorial!
n = int(input())
f = 1
for i in range(1,n):
    f+= f * i
print(f)