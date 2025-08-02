from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
drs, dcs = (1, 0, -1, 0), (0, 1, 0, -1)

start = (0, 0)

def is_melt(grid):
    result = True
    for row in grid:
        result &= (not any(row))

def is_movable(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(grid, start):
    visited = [[False] * m for _ in range(n)]
    visited_nodes = []
    q = deque()
    q.append(start)

    while q:
        row, col = q.popleft()

        if visited[row][col]:
            continue
        visited[row][col] = True
        visited_nodes.append((row, col))
        for dr, dc in zip(drs, dcs):
            nr, nc = row + dr, col + dc
            if is_movable(nr, nc) and grid[nr][nc] == 0:
                q.append((nr, nc))

    return visited_nodes

def melt_iceberg(grid, visited_nodes):
    size = 0
    for node in visited_nodes:
        r, c = node
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if is_movable(nr, nc) and grid[nr][nc] == 1:
                size += 1
                grid[nr][nc] = 0
    return size

time = 0
iceberg_size = 0
while not is_melt(grid):
    visited_nodes = bfs(grid, start)
    time += 1
    iceberg_size = melt_iceberg(grid, visited_nodes)
print(time, iceberg_size)