n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def initialize():
    dp[0][-1] = grid[0][-1]

    for i in range(1, n):
        dp[i][-1] = dp[i - 1][-1] + grid[i][-1]

    for j in range(n - 2, -1, -1):
        dp[0][j] = dp[0][j + 1] + grid[0][j]

initialize()
for i in range(1, n):
    for j in range(n - 2, -1, -1):
        dp[i][j] = min(dp[i][j + 1], dp[i - 1][j]) + grid[i][j]

print(dp[-1][0])