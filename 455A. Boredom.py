M = int(1e5)
a = [0] * (M + 1)
n = int(input())
for x in map(int, input().split()): a[x] += 1
dp = [[0, 0] for _ in range(M + 1)]
for i in range(1, M + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = dp[i - 1][0] + a[i] * i
print(max(dp[M][0], dp[M][1]))