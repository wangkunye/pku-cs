from math import sqrt
def b(x) :
    y=sqrt(x)
    if int(y) == y and y>=2:
        c=[1]*int(y);d=set()
        for k in range(2, int(y)+1) :
            if c[k-2]==1 :
                d.add(k)
                for j in range(k,int(y)+1,k) :
                    c[j-2]=0
        if y in d :
            return 1
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if b(a[i])==1 :
        print('YES')
    else :
        print('NO')
