def q1(x) :
    z=x.index('C');y=[]
    a=int(x[1:z]);b=int(x[z+1:])
    y.append(b//456976)
    b%=456976
    y.append(b//17576)
    b%=17576
    y.append(b//676)
    b%=676
    y.append(b//26)
    y.append(b%26)
    w=0;e=''
    while y[w]==0 :
        w+=1
    v=y[w:];v.reverse();l=[]
    for i in range(len(v)-1):
        if v[i]==0 :
            l.append('Z')
            v[i+1]-=1
            u=i
            while v[u+1]<0 :
                v[u+1]+=26
                v[u+2]-=1
                u+=1
        else :
            l.append(chr(v[i]+64))
    if v[-1]!=0 :
        l.append(chr(v[-1]+64))
    l.reverse();l.append(f'{a}')
    return ''.join(l)
def q2(x) :
    q=w=0
    while 'A'<=x[q]<='Z' :
        q+=1
    y=x[:q];z=int(x[q:])
    k=len(y)-1
    while k>=0 :
        w+=(26**(len(y)-1-k))*(ord(y[k])-64)
        k-=1
    return f'R{z}C{w}'
n=int(input());m=[]
for i in range(n):
    h=input();j=i=0
    while  j<=len(h)-2 and i!=1:
        if h[j].isdigit() and h[j+1].isalpha() :
            i=1
        j+=1
    if i==1 :
        m.append(q1(h))
    else :
        m.append(q2(h))

print('\n'.join(m))