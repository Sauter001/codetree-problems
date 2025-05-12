n, m = map(int, input().split())
area = n * m
grid = [[0] * m for _ in range(n)]

# Please write your code here.
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
count = 1
grid[0][0] = count
cur = (0, 0)
moved = True

def is_movable(r, c):
    return r >= 0 and r < n and c >= 0 and c < m and grid[r][c] == 0

while moved and count <= area:
    moved = False
    for dr, dc in directions:
        while True:
            nr, nc = cur[0] + dr, cur[1] + dc
            # print(nr, nc)
            if not is_movable(nr, nc): 
                break

            count += 1
            grid[nr][nc] = count
            cur = (nr, nc)
            moved = True
            
for row in grid:
    print(*row)