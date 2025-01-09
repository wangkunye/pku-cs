def comb(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c
ans=0

n=int(input())
m=n
k=0
while m>=0 :
    ans+=comb(n,k)
    m-=2
    n-=1
    k+=1
print(ans)