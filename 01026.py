import re
while True:
    n=int(input())
    if n==0 :
        break
    m = list(map(int, input().split()))
    qw=m[:];we=[];ty=1
    for i in range(n):
        we.append(i+1)
    while qw!=we :
        rt=[0 for i in range(n)]
        for i in range(n):
            rt[m[i]-1]=qw[i]
        qw=rt
        ty+=1
    while True:
        a=input()
        if a[0]=='0' :
            break
        p=r'(\d*) (.*)'
        b=re.findall(p,a)
        s=int(b[0][0])%ty
        d=list(b[0][1])
        for i in range(s):
            f = [0 for i in range(n)]
            for j in range(n):
                f[m[j]-1]=d[j]
            d=f
        print(''.join(map(str,d)))