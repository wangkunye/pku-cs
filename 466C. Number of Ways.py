import bisect
n=int(input())
a=list(map(int,input().split()));s=sum(a)
if s%3!=0 :
    print(0)
else :
    b=0;s//=3;c=d=0
    for i in range(n-1):
        c+=a[i]
        if c==2*s :
            b+=d
        if c==s :
            d+=1
    print(b)