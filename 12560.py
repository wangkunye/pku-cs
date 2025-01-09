def q(y,x) :
    if x<2 or x>3 or (y==0 and x==2) :
        return 0
    elif x==3 or (y==1 and x==2):
        return 1
n,m=map(int,input().split());a=[[0]*(m+2)]
for i in range(n) :
    b=[0]+list(map(int,input().split()))+[0]
    a.append(b)
a.append([0]*(m+2))
for i in range(1,n+1) :
    for j in range(1,m+1):
        x=a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1]+a[i][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
        print(q(a[i][j],x),end=' ')
    print('')


