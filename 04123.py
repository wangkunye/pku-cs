t=int(input())
a=[(2,1),(1,2),(2,-1),(-1,2),(-2,1),(1,-2),(-1,-2),(-2,-1)]
def asdf(qwe,x,y) :
    if n * m == qwe:
        global ans
        ans += 1
        return 1
    for w in a :
        s=x+w[0]
        d=y+w[1]
        if b[s][d]==0 and 0<=s<n and 0<=d<m :
            b[s][d]=1
            asdf(qwe+1,s,d)
            b[s][d]=0


for qwrsaf in range(t):
    n,m,x,y=map(int,input().split())
    b=[[0 for i in range(10)] for j in range(10)]
    ans=0
    b[x][y]=1
    asdf(1,x,y)
    print(ans)