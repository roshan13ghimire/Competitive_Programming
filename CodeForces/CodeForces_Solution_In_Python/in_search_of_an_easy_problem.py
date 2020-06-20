#in_search_of_an_easy_problem
n=int(input())
a=list(map(int,input().split()))
if(a.count(1)>=1):
    print("HARD")
else:
    print("EASY")