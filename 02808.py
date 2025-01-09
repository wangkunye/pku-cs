l,m=map(int,input().split())
a=set(range(l+1));jk=set()
for i in range(m):
    b,c=map(int,input().split())
    for k in range(b,c+1):
        if k in a:
            jk.add(k)
print(len(a)-len(jk))