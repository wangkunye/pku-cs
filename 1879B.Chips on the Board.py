t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=sum(a)+min(b)*n;d=sum(b)+min(a)*n
    print(min(c,d))