from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n, k, m = map(int, input().split())
INF = m + 2
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[INF] * n for _ in range(n)]
sources = []
dq = deque()
for _ in range(k):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    dist[r][c] = 0
    sources.append((r, c))
    dq.append((0, r, c))

drs, dcs = (1, 0, -1, 0), (0, 1, 0, -1)

def is_movable(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(grid, sources):
    visited = [[False] * n for _ in range(n)]
    q = deque(sources)

    count = 0
    while q:
        r, c = q.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = True
        count += 1

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not is_movable(nr, nc) or grid[nr][nc] == 1:
                continue
            q.append((nr, nc))
    return count


# 0-1 BFS로 도착할 때 필요한 최소 돌 구하기
while dq:
    cost, r, c = dq.popleft()

    # 더 비용많이 드는 경우는 무시
    if cost > dist[r][c]:
        continue
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if not is_movable(nr, nc):
            continue

        need = grid[nr][nc]    # 0이면 무료, 1이면 돌 하나 부수기
        new_cost = cost + need

        if new_cost < dist[nr][nc]:
            dist[nr][nc] = new_cost
            if need:
                dq.append((new_cost, nr, nc))
            else:
                dq.appendleft((new_cost, nr, nc))

candidate_stones = []

# 후보 돌 골라내기
for i in range(n):
    for j in range(n):
        if dist[i][j] <= m and grid[i][j] == 1:
            candidate_stones.append((i, j))

res = 0
for stones in combinations(candidate_stones, m):
    for si, sj in stones:
        grid[si][sj] = 0
    res = max(res, bfs(grid, sources))

    # 위치 복구
    for si, sj in stones:
        grid[si][sj] = 1

print(res)