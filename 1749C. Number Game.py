import bisect
t=int(input())
for i in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    b.sort()
    if b[0]!=1 :
        print(0)
        continue
    k=ke=min(b.count(1)*2-1,bisect.bisect_right(b,b.count(1)*2-1))
    while True :
        a=b[:]
        j=1
        while j<k :
            q=bisect.bisect_left(a,k-j+1)
            if q==0 :
                break
            a[0]+=k-j+1
            a.sort()
            if a[0]!=1 :
                break
            j+=1
        if j<k :
            ke-=1
            k=ke
            continue
        else :
            break
    print(ke)