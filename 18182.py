nqwe=int(input())
for i in range(nqwe):
    n,m,b=map(int,input().split())
    a=[]
    for k in range(n):
        a.append(list(map(int,input().split())))
    a.sort(key=lambda x:(x[0],-x[1]))
    q=a[0][0]
    w=0
    for j in range(n):
        if a[j][0]>q:
            w=0
            q=a[j][0]
        w+=1
        if w>m :
            continue
        b-=a[j][1]
        if b<=0 :
            break
    if b>0 :
        print('alive')
    else :
        print(q)