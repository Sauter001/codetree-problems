import sys

n = int(input())
input = sys.stdin.readline
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    s = 0
    for j in range(1, i + 1):
        s += dp[j - 1] * dp[i - j]
    dp[i] = s
print(dp[n])