#Transform_the_Expression
for _ in range(int(input())):
    s=input()
    l='+*^-%/'
    ss=''
    st=[]
    for i in s:
        if(i in l):
            st.append(i)
        elif(i>='a' and i<='z'):
            ss+=i
        elif(i==')'):
            ss+=st.pop()
    print(ss)
                