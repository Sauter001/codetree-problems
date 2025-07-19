from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[False] * n for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

count = 0
def bfs(start, visited, grid):
    global count
    def is_movable(i, j):
        return 0 <= i < n and 0 <= j < n

    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()

        if visited[cur[0]][cur[1]]:
            continue
        
        count += 1
        visited[cur[0]][cur[1]] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = cur[0] + dx, cur[1] + dy
            if is_movable(nx, ny) and not grid[nx][ny]:
                q.append((nx, ny))


for p in points:
    p = (p[0] - 1, p[1] - 1)
    bfs(p, visited, grid)
print(count)