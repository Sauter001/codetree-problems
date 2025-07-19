from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

result = False
q = deque()
q.append((0, 0))

def is_movable(i, j):
    return 0 <= i < n and 0 <= j < m

while q:
    cur = q.popleft()
    if cur == (n - 1, m - 1):
        result = True
    
    if visited[cur[0]][cur[1]]:
        continue

    visited[cur[0]][cur[1]] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = cur[0] + dx, cur[1] + dy
        if is_movable(nx, ny) and grid[ny][ny]:
            q.append((nx, ny))

print(1 if result else 0)