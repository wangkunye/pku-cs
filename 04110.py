n,w=map(int,input().split())
a=[[0,0] for i in range(n)]
for i in range(n):
    a[i][0],a[i][1]=map(int,input().split())
    a[i][0]=a[i][0]/a[i][1]
a=sorted(a);a.reverse();b=c=d=0
while c<w and b<n:
    if c+a[b][1] <=w :
        c+=a[b][1]
        d+=a[b][0]*a[b][1]
    else :
        d+=a[b][0]*(w-c)
        c=w
    b+=1
print('%.1f'%d)
