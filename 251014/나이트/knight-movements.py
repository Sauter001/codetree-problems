from collections import deque

n = int(input())
positions = map(int, input().split())
positions = [p - 1 for p in positions]
r1, c1, r2, c2 = positions # 위치 -1 평행 이동

visited = [[0] * n for _ in range(n)]
distances = [[-1] * n for _ in range(n)]

res = -1

# BFS
def movable(r, c):
    return 0 <= r < n and 0 <= c < n

def move(r, c, step):
    visited[r][c] = True
    distances[r][c] = step

q = deque([(r1, c1)])
move(r1, c1, 0)
dirs = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
while q:
    r, c = q.popleft()
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if movable(nr, nc) and not visited[nr][nc]:
            move(nr, nc, distances[r][c] + 1)
            q.append((nr, nc))


print(distances[r2][c2])


