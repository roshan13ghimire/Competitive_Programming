#Anton_and_Polyhedrons
n=int(input())
c=0
for i in range(n):
    a=input()
    if(a=='Tetrahedron'):
        c+=4
    elif(a=='Cube'):
        c+=6
    elif(a=='Octahedron'):
        c+=8
    elif(a=='Dodecahedron'):
        c+=12
    else:
        c+=20
print(c)        