#Roy_and_Profile_Picture
l = int(input())
n = int(input())
for _ in range(n):
    w , h = map(int,input().split())
    if w < l or h < l:
        print("UPLOAD ANOTHER")
    elif (w >= l and  h >= l) and (h != w):
        print("CROP IT")
    elif (h >= l and w >= l) and (h == w) :
        print("ACCEPTED")