from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
drs, dcs = (1, 0, -1, 0), (0, 1, 0, -1)

start = (0, 0)

def is_movable(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs(grid, start):
    visited = [[False] * m for _ in range(n)]
    visited_nodes = []
    melting_now = set()
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
            if is_movable(nr, nc):
                if grid[nr][nc] == 0:
                    q.append((nr, nc))
                elif grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    melting_now.add((nr, nc))

    return melting_now

time = 0
iceberg_size = 0

while True:
    # 매 턴마다, (0,0)에서부터 다시 탐색해서 현재 물에 닿은 빙하 찾기
    melting_now = bfs(grid, start)

    # 더 녹을 빙하가 없으면 끝
    if not melting_now:
        break

    time += 1
    iceberg_size = len(melting_now)
    for r, c in melting_now:
        grid[r][c] = 0

print(time, iceberg_size)