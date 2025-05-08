n = int(input())
rects = []
xs, ys = [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    xs += [a, c]
    ys += [b, d]
    rects.append(('r', a, b, c, d) if i % 2 == 0 else ('b', a, b, c, d))

# Please write your code here.
xs.sort()
ys.sort()

xmap = {x:i for i, x in enumerate(xs)} 
ymap = {y:i for i, y in enumerate(ys)}

width, height = len(xs), len(ys)

grid = [[0] * height for _ in range(width)]

for color, x1, y1, x2, y2 in rects:
    xi1, yi1 = xmap[x1], ymap[y1]
    xi2, yi2 = xmap[x2], ymap[y2]

    for xi in range(xi1, xi2):
        for yi in range(yi1, yi2):
            grid[xi][yi] = 1 if color == 'r' else -1

area = 0
for i in range(width - 1):
    for j in range(height - 1):
        if grid[i][j] == -1:
            dx = xs[i + 1] - xs[i]
            dy = ys[j + 1] - ys[j]
            area += dx * dy

print(area)