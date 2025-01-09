p=int(input())
a=list(map(int,input().split()))
a.sort()
if p<a[0] :
    print(0)
else :
    n=len(a)-1
    i=0;j=n;e=0
    while i<=j:
        if p>=a[i] :
            p-=a[i]
            i+=1
            e+=1
        elif p+a[j]>a[i] :
            p=p+a[j]-a[i]
            j-=1
            i+=1
        else :
            break
    print(e)