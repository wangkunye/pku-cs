import bisect
m=int(input())
for i in range(m):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(range(n,0,-1))
    for i in range(k):
        if a==b :
            a=list(range(1,n+1))
            continue
        q=n-2;w=a[-1];qw=[a[-1]]
        while a[q]>w :
            qw.append(a[q])
            w=max(w,a[q])
            q-=1
        qw.sort()
        s=bisect.bisect_left(qw,a[q])
        asd=a.index(qw[s])
        a[asd]=a[q]
        a[q]=qw[s]
        a=a[:q+1]+sorted(a[q+1:])
    print(' '.join(map(str,a)))