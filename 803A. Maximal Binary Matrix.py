import sys
n,k=map(int,input().split())
if k>n*n :
    print(-1)
    sys.exit()
a=[[0 for j in range(n)] for i in range(n)]
i=j=0
while i<n and k>0 :
    if i==j :
        a[i][j]=1
        k-=1
        j+=1
        continue
    if k==1 :
        if i<n-1 :
            a[i+1][i+1]=1
            k-=1
        break
    a[i][j]=1
    a[j][i]=1
    k-=2
    j+=1
    if j==n :
        i+=1
        j=i
if k==0 :
    for i in a :
        print(' '.join(map(str,i)))
else :
    print(-1)