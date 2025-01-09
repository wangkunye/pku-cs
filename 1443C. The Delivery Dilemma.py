t=int(input());h=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[];d=[];q=w=0
    for j in range(n):
        if a[j]<=b[j]:
            q=max(q,a[j])
        else :
            w+=b[j]
            c.append(a[j])
            d.append(b[j])
    if q>=w or q>=max(c):
        h.append(q)
        continue
    elif  min(c)>=w:
        h.append(w)
        continue
    else:
        e=list(zip(c,d))
        e.sort();e.reverse();f=len(e)-1;g=0
        while f>=0 and g<e[f][0]:
            g+=e[f][1]
            f-=1
        h.append(min(w,e[f+1][0]))
print('\n'.join(map(str,h)))
