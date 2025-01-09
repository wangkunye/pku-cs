q,w=map(int,input().split());a=[]
for i in range(q):
    a.append([int(x) for x in input().split()])
e,r=map(int,input().split())
if w!=e :
    print("Error!")
else :
    b=[]
    for i in range(e):
        b.append([int(x) for x in input().split()])
    t, y = map(int, input().split())
    if t != q or r != y:
        print("Error!")
    else:
        c = []
        for i in range(t):
            c.append([int(x) for x in input().split()])
        d=[[0 for i in range(r)] for j in range(q)]
        for i in range(q):
            for j in range(r):
                for k in range(w):
                    d[i][j]+=a[i][k]*b[k][j]
                d[i][j]+=c[i][j]
                if j<r-1 :
                    print(d[i][j],end=' ')
                else :
                    print(d[i][j])
