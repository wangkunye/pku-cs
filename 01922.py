while True :
    N=int(input());a=[]
    if N==0 :
        break
    for i in range(N):
        a.append([int(x) for x in input().split()])
    for i in range(N):
        if a[i][1]>=0 :
            b=c=a[i:]
            break
    for i in b[1:]:
        if i[1]<0:
            c.remove(i)
    from math import ceil
    d=[]
    for i in c:
        d.append(16200/i[0]+i[1])
    print(ceil(min(d)))



