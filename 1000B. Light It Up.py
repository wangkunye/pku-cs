import sys
n,t=map(int,input().split())
a=[0]+list(map(int,input().split()))
a+=[t]
b=[];c=[];i=0
while i<len(a)-1 :
    if i%2==0 :
        b.append(a[i+1]-a[i])
    else :
        c.append(a[i+1]-a[i])
    i+=1
e=max(c);q=sum(b)
if e==1 :
    print(q)
    sys.exit()
w=sum(c);r=0;y=q;u=0
while r<len(c):
    u+=b[r]
    if w-1>q-u :
        y=max(y,u+w-1)
    w-=c[r]
    q-=b[r]
    r+=1
print(y)