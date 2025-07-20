n = int(input())
MAX_LIMIT = 1000
dp = [0] * (MAX_LIMIT + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)
