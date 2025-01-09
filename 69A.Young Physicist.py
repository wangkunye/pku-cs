n=int(input());a=b=c=0
for i in range(n):
    cnm=list(map(int,input().split()))
    a+=cnm[0];b+=cnm[1];c+=cnm[2]
if a==b==c==0 :
    print('YES')
else :
    print('NO')
