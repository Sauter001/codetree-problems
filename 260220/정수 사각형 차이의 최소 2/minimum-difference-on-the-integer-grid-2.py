import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def can_reach_any(diff):
    for start in set(sum(grid, [])):
        if can_reach(start, diff):
            return True
    return False

def can_reach(start, diff):
    def in_range(val):
        return start <= val <= start + diff

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        if not in_range(grid[i][0]):
            break
        dp[i][0] = 1
    for i in range(n):
        if not in_range(grid[0][i]):
            break
        dp[0][i] = 1
    
    for i in range(1, n):
        for j in range(1, n):
            if in_range(grid[i][j]):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    if dp[n-1][n-1] > 0:
        return True

    return False
    
min_val = min(min(row) for row in grid)
max_val = max(max(row) for row in grid)

low, high = 0, max_val - min_val
while low < high:
    mid = (low + high) // 2
    if can_reach_any(mid):
        high = mid
    else:
        low = mid + 1
print(low)