t=int(input());e=[];g=[];c=o=0;l=''
for k in range(1,33000) :
    l+=str(k)
    c+=len(str(k))
    o+=c
    g.append(o)
import bisect
for i in range(t):
    a=int(input())
    q=bisect.bisect_left(g,a)
    if g[q]!=a :
        e.append(l[a-g[q-1]-1])
    else :
        e.append(l[q])
print('\n'.join(map(str,e)))
