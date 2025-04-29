from collections import defaultdict

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dirs = []
for num, direction in commands:
    x.append(int(num))
    dirs.append(direction)

# Please write your code here.

tiles = defaultdict(list)
tile_colors = {'w':0, 'b':0, 'g':0} # (흰색, 검은색, 회색)
cursor = 0

for i, v, d in zip(range(1, n + 1), x, dirs):
    new_position = 0
    if d == 'L':
        new_position = cursor - v + 1
        for pos in range(new_position, cursor + 1):
            tiles[pos].append((i, 'w'))
    elif d == 'R':
        new_position = cursor + v - 1
        for pos in range(cursor, new_position + 1):
            tiles[pos].append((i, 'b'))
    cursor = new_position
# print(tiles)

# 타일 색 결정
for i, paints in tiles.items():
    if len(paints) <= 3:
        tile_colors[paints[-1][1]] += 1
    else:
        bs, ws = 0, 0
        for p in paints:
            if p[1] == 'b':
                bs += 1
            else:
                ws += 1
        if bs >= 2 and ws >= 2:
            tile_colors['g'] += 1
        else:
            tile_colors[paints[-1][1]] += 1
print(tile_colors['w'], tile_colors['b'], tile_colors['g'])
