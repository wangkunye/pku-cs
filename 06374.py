n=int(input())
a=list(map(str,input().split()));b=[]
for i in range(n):
    if sum(len(x) for x in b)+len(b)<70 :
        b.append(a[i])
    else :
        print(b)
        b.clear()
        b.append(a[i])
if len(b)>0:
    for k in range(len(b)):
        if k < len(b)-1:
            print(b[k], end=' ')
        else:
            print(b[k])