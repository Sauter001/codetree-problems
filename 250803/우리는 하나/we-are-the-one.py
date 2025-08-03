from itertools import combinations
from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
candidates = [(i, j) for i in range(n) for j in range(n)]

drs, dcs = (1, 0, -1, 0), (0, 1, 0, -1)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(row, col):
    visited = [[False] * n for _ in range(n)]
    visited_set = set()
    q = deque([(row, col)])

    while q:
        r, c = q.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = True
        visited_set.add((r, c))
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and u <= abs(grid[r][c] - grid[nr][nc]) <= d:
                q.append((nr, nc))
    return visited_set

count = 0
for sources in combinations(candidates, k):
    visited_position_set = set()
    for sr, sc in sources:
        visited_set = bfs(sr, sc)
        visited_position_set |= visited_set
    count = max(count, len(visited_position_set))

print(count)

