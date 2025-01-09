n,m=map(int,input().split())
a=list(map(int,input().split()))
qw=[10**6+1 for i in range(m+1)]
qw[0]=0
for i in range(1,m+1):
    for j in a :
        if i>=j :
            qw[i]=min(qw[i],qw[i-j]+1)
if qw[m]!=10**6+1:
    print(qw[m])
else :
    print(-1)