n,m=map(int,input().split())
a=[['.' for i in range(m+2)]]
for qw in range(n):
    a.append(['.']+list(input())+['.'])
a.append(['.' for i in range(m+2)])
ans=0
for i in range(1,n+1) :
    for j in range(1,m+1):
        if a[i][j]=='.':
            continue
        if a[i-1][j-1]=='.' and a[i-1][j]=='.' and a[i-1][j+1]=='.' and a[i][j-1]=='.' and a[i][j+1]=='.' and a[i+1][j-1]=='.' and a[i+1][j]=='.' and a[i+1][j+1]=='.' and a[i][j]=='W':
            ans+=1
            continue
        if a[i-1][j-1]!='.' or a[i-1][j]!='.' or a[i-1][j+1]!='.' or a[i+1][j-1]==1 or a[i][j-1]!='.':
            if  a[i+1][j+1]=='W':
                a[i+1][j+1]=1
            continue
        if a[i][j+1]=='W'  or a[i+1][j]=='W' or a[i+1][j+1]=='W' or a[i+1][j-1]=='W':
            ans+=1
            if a[i+1][j+1]=='W' :
                a[i+1][j+1]=1
print(ans)