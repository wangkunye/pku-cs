q,w,e=map(int,input().split())
a=[[0]*q for i in range(q)]
b=[[0]*q for i in range(q)]
d=[[0]*q for i in range(q)]
for i in range(w) :
    z,x,c=map(int,input().split())
    a[z][x]=c
for i in range(e):
    z,x,c=map(int,input().split())
    b[z][x]=c
for i in range(q):
    for j in range(q):
        for k in range(q):
            d[i][j]+=a[i][k]*b[k][j]
        if d[i][j]!=0 :
            print(i,j,d[i][j])
