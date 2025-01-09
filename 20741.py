n=int(input())
q=[-1,0,0,1]
w=[0,-1,1,0]
cnt=[]
e=0

def qwer(a,x,y) :
    global e

    if a[x][y]=='1' :
        a[x][y]=-1
        for i in range(4):
            qwer(a,x+q[i],y+w[i])
        cnt.append(e)
        e=0
    if a[x][y]=='0' :
        a[x][y]=-2
        e+=1
        for i in range(4):
            qwer(a,x+q[i],y+w[i])
        e-=1

a=[[-1 for i in range(n+2)]]
for i in range(n):
    a.append([-1]+list(input())+[-1])
a.append([-1 for i in range(n+2)])
qwer(a,1,1)
for i in range(len(cnt)) :
    if cnt[i]==0 :
        cnt[i]+=9999999
print(min(cnt))