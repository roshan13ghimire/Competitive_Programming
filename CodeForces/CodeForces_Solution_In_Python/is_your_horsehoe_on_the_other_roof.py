#is_your_horsehoe_on_the_other_roof
s1,s2,s3,s4=map(int,input().split())
s=[]
s.append(s1)
s.append(s2)
s.append(s3)
s.append(s4)
print(4-len(set(s)))