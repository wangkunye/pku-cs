n,m=map(int,input().split());a=set()
for i in range(n):
    b=list(map(int,input().split()))
    for j in b[1:] :
        a.add(j)
if len(a)==m:
    print('YES')
else :
    print('NO')