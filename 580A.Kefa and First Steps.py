n=int(input())
m=list(map(int,input().split()))
a=1;b=[]
for i in range(0,n-1):
    if m[i]<=m[i+1]:
        a+=1
    else :
        b.append(a)
        a=1
        continue
b.append(a)
print(max(b))