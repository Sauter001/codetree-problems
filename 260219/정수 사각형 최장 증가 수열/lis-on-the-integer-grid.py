import sys

sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
drs, dcs = (0, 1, 0, -1), (1, 0, -1, 0)

def pos_movable(p):
    return 0 <= p < n

def movable(r, c):
    return pos_movable(r) and pos_movable(c)

def find_recursively(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    candidate_positions = []
    for dr, dc in zip(drs, dcs):
        nr, nc = i + dr, j + dc
        if not movable(nr, nc):
            continue
        if grid[nr][nc] > grid[i][j]:
            candidate_positions.append((nr, nc))
    candidate_vals = []
    for cr, cc in candidate_positions:
        candidate_vals.append(find_recursively(cr, cc))
    if candidate_vals:
        dp[i][j] = 1 + max(candidate_vals)
    else:
        dp[i][j] = 1
    return dp[i][j]

for i in range(n):
    for j in range(n):
        find_recursively(i, j)
print(max(max(row) for row in dp))