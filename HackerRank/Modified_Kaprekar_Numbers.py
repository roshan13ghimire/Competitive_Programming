#Modified_Kaprekar_Numbers
p=int(input())
q=int(input())
l=[]
if(p==1):
    l.append(p)
for i in range(p,q+1):
    c=str(i*i)
    a=c[:len(c)//2]
    b=c[len(c)//2:]
    if(len(a)!=0):
        if(int(a)+int(b)==i):
            l.append(str(i))
if(len(l)!=0):
    print(' '.join([str(i) for i in l]))
else:
    print("INVALID RANGE")
    
    
# Flag Solution in C++
# #include <cmath>
# #include <cstdio>
# #include <vector>
# #include <iostream>
# #include <algorithm>
# using namespace std;

# int main() {
#     long int p,q;
#     cin>>p>>q;
#     int flag=0;
#     for(long int t=p;t<=q;t++)
#         {
        
#         if(t==0)
#             {
#             cout<<t;
            
#         }
#         else if(t==10||t==100||t==1000||t==10000)
#             {
#             continue;
#         }
#         else{
#              long int n=1;
#             for( long int i=10;i<=t;i=i*10)
#                 {
#                 n=i;
#             }
#             n=n*10;
#              long int s=t*t;
#             if((s%n)+(s/n)==t)
#                 {
#                 flag=1;
#                 cout<<t<<" ";
#             }    
#         }
#     }
#     if(flag==0)
#         {
#         cout<<"INVALID RANGE";
#     }
#     return 0;
# }
