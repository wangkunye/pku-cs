m=n=int(input())
d=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append((i+1,d[i]))
a.sort(key=lambda x: x[1])
b=[];c=0
n-=1
while n>=0 :
    b.append(a[m-1-n][0])
    c+=n*a[m-1-n][1]
    n-=1
print(' '.join(map(str,b)))
print('%.2f'%(c/m))