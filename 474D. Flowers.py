# 成组放置问题
MOD = 1000000007
MAXN = 100001

t, k = map(int, input().split())

f = [0] * MAXN
f[0] = 1
s = [0] * MAXN
for i in range(1, 100001):
    if i >= k:
        f[i] = (f[i-1] + f[i - k]) % MOD
    else:
        f[i] = f[i - 1]
        #f[i] = 1

    s[i] = (s[i - 1] + f[i]) % MOD

for _ in range(t):
    a, b = map(int, input().split())
    print((s[b] - s[a - 1] + MOD) % MOD)
