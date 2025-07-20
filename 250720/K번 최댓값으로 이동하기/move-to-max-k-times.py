from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1

def bfs(start):
    def movable(i, j):
        return 0 <= i < n and 0 <= j < n

    result = []
    visited = [[False] * n for _ in range(n)]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque([start])
    critical = grid[start[0]][start[1]] # 기준치(이보다 작은 값만 이동 가능)

    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue
        
        visited[x][y] = True
        result.append((x, y))
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if movable(nx, ny) and grid[nx][ny] < critical:
                q.append((nx, ny))
    result.pop(0) # 시작 노드 제거
    return result

def find_new_pos(positions):
    values = {grid[r][c] for r, c in positions}
    max_val = max(values)

    # 최대 수 있는 위치만 걸러내기
    positions = list(filter(lambda p: grid[p[0]][p[1]] == max_val, positions))
    positions.sort()
    return positions[0]


for i in range(k):
    searched_list = bfs((r, c))
    if searched_list:
        r, c = find_new_pos(searched_list)
    else:
        break
print(r + 1, c + 1)
