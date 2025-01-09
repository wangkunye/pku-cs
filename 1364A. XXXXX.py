t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=sum(a)
    if b%m!=0 :
        print(n)
    elif a[0]%m!=0 or a[-1]%m!=0 :
        print(n-1)
    else:
        q=1;c=False
        while a[q-1]%m==0 and a[-q]%m==0 :
            q+=1
            if q==(n//2)+1 or q>=n:
                c=True
                break
        if c :
            print(-1)
        else:
            print(n-q)

