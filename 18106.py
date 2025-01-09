n=int(input())
a=[[-1 for i in range(n+2)]]
for i in range(n):
    a.append([-1]+[0 for i in range(n)]+[-1])
a.append([-1 for i in range(n+1)])
b=[[0,1],[1,0],[0,-1],[-1,0]]
i=j=e=1
k=0
while e<=n*n :
    a[i][j]=e
    if a[i+b[k][0]][j+b[k][1]]!=0 :
        k+=1
        if k==4 :
            k-=4
    i+=b[k][0]
    j+=b[k][1]
    e+=1
for i in range(1,n+1) :
    print(' '.join(map(str,a[i][1:n+1])))