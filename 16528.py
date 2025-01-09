n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort(key=lambda x:(x[0],x[1]))
end=a[0][1]
ans=1
for i in range(1,n):
    if a[i][0]>end:
        ans+=1
        end=a[i][1]
    else :
        end=min(end,a[i][1])
print(ans)