n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
i=0;y=-10**9-1;e=1
while i<n-1 :
    if a[i][0]-a[i][1]>y :
        y=a[i][0]
        e+=1
    elif a[i][0]-a[i][1]<=y and a[i][0]+a[i][1]>=a[i+1][0] :
        y=a[i][0]
    else :
        y=a[i][0]+a[i][1]
        e+=1
    i+=1
print(e)