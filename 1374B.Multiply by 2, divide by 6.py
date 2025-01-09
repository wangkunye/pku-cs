t=int(input())
for i in range(t):
    a=int(input());b=0;c=0
    while a>0 and a%2==0:
        a/=2;b+=1
    while a>0 and a%3==0:
        a/=3;c+=1
    if a==1 and b<=c :
        print(2*c-b)
    else :
        print(-1)