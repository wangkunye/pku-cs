n=int(input())
a=[[-1 for i in range(n+2)]]
for i in range(n):
    a.append([-1]+list(map(int,input().split()))+[-1])
a.append([-1 for i in range(n+1)])
b=[0,1,0,-1]
c=[1,0,-1,0]
i=j=e=1
k=0
ans=[0 for i in range(n)]
r=0
while e<=n*n :
    ans[r]+=a[i][j]
    a[i][j]=-1
    if a[i+b[k]][j+c[k]]==-1 :
        k+=1
        if k==4 :
            k-=4
            r+=1
    i+=b[k]
    j+=c[k]
    e+=1
print(max(ans))