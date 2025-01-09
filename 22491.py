h=int(input())
m=int(input())
h=2*h-m/2
a=[]
for i in range(m):
    x,y=map(float,input().split())
    a.append([x,y])
a.sort(key=lambda x: x[1]*x[0])
a.reverse();b=c=0
while h>0 and b<m :
    q=5/a[b][0]
    if q<=h :
        c+=5*a[b][1]
        h-=q
    else :
        c+=h*a[b][1]*a[b][0]
        h=0
    b+=1
print(round(c,1))