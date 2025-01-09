t=int(input())
a=list(map(int,input().split()))
b=0;c=0;num=1
for i in a:
    if i%2==0:
        b+=1
    else :
        c+=1
if b>c:
    for i in a:
        if i%2==0:
            num+=1
        else :
            break
else :
    for i in a:
        if i%2==1:
            num+=1
        else :
            break
print(num)