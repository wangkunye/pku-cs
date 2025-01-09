a,b,k=map(int,input().split())
q=[[1 for x in range(b+2)] for y in range(a+2)]
for x in range(k):
    r,s,p,t=map(int,input().split());p//=2
    w=r-p;e=s-p;f=r+p+1;g=s+p+1
    if w<0 :
        w=0
    if e<0:
        e=0
    if f>a+2 :
        f=a+2
    if g>b+2 :
        g=b+2
    if t==0 :
        for i in range(w,f):
            for j in range(e,g):
                q[i][j]=0
    else :
        for i in range(w,f):
            for j in range(e,g):
                if q[i][j]==0:
                    continue
                else:
                    q[i][j]+=1

ui=2;io=0
for i in range(1,a+1):
    for j in range(1,b+1):
        if q[i][j]>ui:
            ui=q[i][j]
            io=0
        if q[i][j]==ui:
            io+=1
print(io)