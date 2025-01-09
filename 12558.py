n,m=map(int,input().split())
a=[[0 for i in range(m+2)]]
for i in range(n):
    a.append([0]+list(map(int,input().split()))+[0])
a.append([0 for i in range(m+2)])
b=[[-1,0],[0,-1],[1,0],[0,1]]
ans=0
for i in range(1,n+1) :
    for j in range(1,m+1):
        if a[i][j]==0 :
            continue
        s=4
        for k in b :
            if a[i+k[0]][j+k[1]]==1 :
                s-=1
        ans+=s
print(ans)