n=int(input())
a=list(map(int,input().split()))
b=[0 for i in range(n)]
c=[1 for i in range(n)]
i=1
while i<n :
    j=i-1
    big=1
    sma=1
    while j>=0 :
        if big>1 and sma>1 :
            break
        if a[i]>a[j] and b[j]==1 or a[i]<a[j] and b[j]==-1 or a[i]==a[j] :
            j-=1
            continue
        if a[i]>a[j] and b[j]!=1 :
            big=max(c[j]+1,big)
            j-=1
            continue
        if a[i]<a[j] and b[j]!=-1 :
            sma=max(c[j]+1,sma)
            j-=1
            continue
    if big>=sma :
        c[i]=big
        b[i]=1
    else :
        c[i]=sma
        b[i]=-1
    i+=1
print(c[-1])