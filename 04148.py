j=1
while True:
    a,b,c,d=map(int,input().split())
    if a==-1:
        break
    a%=23;b%=28;c%=33
    x=set();q=0
    while q<=28*33 :
        x.add(23*q+a);q+=1
    y=set();w=0
    while w<=23*33:
        y.add(28*w+b);w+=1
    z=set();e=0
    while e<=23*28 :
        z.add(33*e+c);e+=1
    f=x&y&z
    if 0 in f :
        f.remove(0)
    u=min(f)
    if u<d :
        u+=21252
    print(f'Case {j}: the next triple peak occurs in {u-d} days.')
    j+=1
