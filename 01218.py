t=int(input())
for i in range(t):
    n=int(input())
    a=[0]*(n+1);b=1
    while b<=n:
        for k in range(0,n+1,b) :
            a[k]=1-a[k]
        b+=1
    print(sum(a[1:]))

