n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
num=0
for i in range(m):
    if a[i]>0:
        break
    else :
        num+=a[i]
print(-num)