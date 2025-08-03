from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
steps = [[0] * m for _ in range(n)]
dxs, dys = (1, 0, -1, 0), (0, 1, 0, -1)

visited = [[False] * m for _ in range(n)]
q = deque([(0, 0)])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def push(x, y, s):
    steps[x][y] = s
    visited[x][y] = True
    q.append((x, y))

push(0, 0, 0)
steps[n - 1][m - 1] = -1
while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
            push(nx, ny, steps[x][y] + 1)

print(steps[n - 1][m - 1])

