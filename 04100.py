k=int(input())
for i in range(k):
    n=t=int(input());a=[]
    for j in range(t):
        j,k=map(int,input().split())
        a.append((j,k))
    a.sort(key=lambda x:(x[1],x[0]));m=a[0][1]
    for y in range(t-1) :
        if a[y+1][0]<=m and a[y+1][0]<=a[y][1]:
            n-=1
        else :
            m=a[y+1][1]
    print(n)
