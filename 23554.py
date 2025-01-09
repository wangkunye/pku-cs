n=int(input());b=list(range(1,n+1));c=[]
a=list(map(int,input().split()))
for i in a:
    if i in range(1,n+1):
        b.remove(i)
    else :
        c.append(i)
for i in b :
    print(i,end=' ')
print()
for i in sorted(c) :
    print(i,end=' ')