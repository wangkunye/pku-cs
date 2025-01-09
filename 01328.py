import math
g=1
while True :
    n,d=map(int,input().split())
    if n==d==0 :
        break
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    hjk=input()
    a.sort(key=lambda x:x[1])
    if a[-1][1]>d or d<=0:
        print(f'Case {g}: {-1}')
        g+=1
        continue
    a.sort(key=lambda x:(x[0],-x[1]))
    b=0;e=0;right=-10000000000
    while b<n :
        c=a[b][0]-math.sqrt(math.pow(d,2)-math.pow(a[b][1],2));v=a[b][0]+math.sqrt(math.pow(d,2)-math.pow(a[b][1],2))
        if c>right :
            e+=1
            right=v
        else :
            right=min(v,right)
        b+=1
    print(f'Case {g}: {e}')
    g+=1