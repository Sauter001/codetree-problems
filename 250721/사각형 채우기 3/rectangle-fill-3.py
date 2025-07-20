import sys
input = sys.stdin.readline

n = int(input())
MAX_VAL = 1000
dp = [0] * (MAX_VAL + 1)

dp[0] = 1
dp[1] = 2
dp[2] = 7

for i in range(3, n + 1):
    dp[i] = 3 * dp[i - 1] + dp[i - 2] - dp[i - 3]

print(dp[n] % 1_000_000_007)