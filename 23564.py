n=int(input())
a=[];b=set()
for i in range(2,n+1):
    while n>1 and n%i==0:
        n/=i
        a.append(i);b.add(i);
if len(a)==len(b) :
    if len(b)%2==0 :
        print(1)
    else :
        print(-1)
else :
    print(0)



