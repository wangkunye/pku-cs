t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[0]*n;b.sort()
    d=[(a[h],h) for h in range(n)];d.sort()
    for g in range(n):
        c[d[g][1]]=b[g]
    for x in c:
        print(x,end=' ')
        print()
