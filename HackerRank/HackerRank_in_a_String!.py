#HackerRank_in_a_String!
def hackerrankInString(s):
    sub = "hackerrank"
    j = 0
    for p in s:
        if p == sub[j]:
            j += 1
            if j == len(sub):
                return "YES"
    return "NO"
for _ in range(int(input())):
    s = input()
    print(hackerrankInString(s))
            