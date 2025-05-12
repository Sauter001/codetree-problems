n, m = map(int, input().split())
placeholder = '?'
grid = [[placeholder] * m for _ in range(n)]

directions = [(0,1), (1,0), (0,-1), (-1,0)]  # → ↓ ← ↑

# Please write your code here.
def num_to_alphabet(x: int):
    return chr(65 + ((x - 1) % 26))

r, c, d = 0, 0, 0
for cnt in range(1, n*m + 1):
    grid[r][c] = num_to_alphabet(cnt)
    nr, nc = r + directions[d][0], c + directions[d][1]

    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == placeholder:
        r, c = nr, nc
    else:
        d = (d + 1) % 4
        r, c =  r + directions[d][0], c + directions[d][1]

for r in grid:
    print(*r)
