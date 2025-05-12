n = int(input())
area = n * n
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
grid = [[0] * n for _ in range(n)]

# Please write your code here.
r, c, d = n - 1, n - 1, 0

def movable(r, c):
    return 0 <= r < n and 0 <= c < n and grid[r][c] == 0

for cnt in range(area):
    grid[r][c] = area - cnt
    nr, nc = r + directions[d][0], c + directions[d][1]
    
    if movable(nr, nc):
        r, c = nr, nc
    else:
        d = (d + 1) % 4
        r, c = r + directions[d][0], c + directions[d][1]

for r in grid:
    print(*r)
