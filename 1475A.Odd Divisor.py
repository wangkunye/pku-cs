t=int(input())
for i in range(t):
    a=int(input())
    while a>1 and a%2==0:
        a/=2
    if a==1:
        print('NO')
    else :
        print('YES')
