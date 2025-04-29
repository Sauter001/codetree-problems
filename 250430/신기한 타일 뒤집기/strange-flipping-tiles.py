n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
xs = []
dirs = []
for num, direction in commands:
    xs.append(int(num))
    dirs.append(direction)

# Please write your code here.
MAX_POS = 10 ** 5
pos = [0] * (2 * MAX_POS + 1)
cursor = 0
left, right = 0, 0

for x, d in zip(xs, dirs):
    if d == 'L':
        while x:
            pos[cursor] = -1
            cursor -= 1
            x -= 1
        cursor += 1
        left = min(cursor, left)
    else:
        while x:
            pos[cursor] = 1
            cursor += 1
            x -= 1
        cursor -= 1
        right = max(cursor, right)

compressed_pos = [pos[i] for i in range(left, right + 1)]
counter = {1: 0, -1: 0}
for x in compressed_pos:
    counter[x] += 1
print(counter[-1], counter[1])

