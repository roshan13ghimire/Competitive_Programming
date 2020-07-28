#Jumping_on_the_Clouds
def jumpingOnClouds(a):
    i = 0
    c = 0
    while i < n - 1:
        if i < n - 2 and a[i + 2] == 0:
            i += 2
        else:
            i += 1
        c += 1
    return c
n = int(input())
a = list(map(int,input().split()))
print(jumpingOnClouds(a))