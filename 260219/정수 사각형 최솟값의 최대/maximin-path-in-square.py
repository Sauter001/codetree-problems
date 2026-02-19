n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = grid[0][0]
MAX_VAL = 1000000

def print_2d(arr):
    for row in arr:
        print(*row)

mr = mc = MAX_VAL
for i in range(n):
    mr = min(mr, grid[i][0])
    mc = min(mc, grid[0][i])

    dp[0][i] = mc
    dp[i][0] = mr

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(grid[i][j], max(dp[i - 1][j], dp[i][j - 1]))

print(dp[n-1][n-1])