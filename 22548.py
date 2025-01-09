a=list(map(int,input().split()))
t=a[0]
b=[max(a[1:])-a[0]]
for i in range(1,len(a)-1) :
    if a[i]>=t :
        continue
    else :
        b.append(max(a[i+1:])-a[i])
        t=a[i]
q=max(b)
if q>0 :
    print(q)
else :
    print(0)