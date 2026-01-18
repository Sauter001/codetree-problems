n, k = map(int, input().split())
MAX_VAL = 10000
coordinate = ['X'] * (MAX_VAL + 1)
positions = []
signs = []
for _ in range(n):
    pos, sign = input().split()
    positions.append(int(pos))
    signs.append(sign)

for pos, sign in zip(positions, signs):
    coordinate[pos] = sign

res = 0
for start in range(MAX_VAL - (k - 1)):
    candidate = 0
    for i in range(start, start + k + 1):
        if coordinate[i] == 'G':
            candidate += 1
        elif coordinate[i] == 'H':
            candidate += 2
    res = max(res, candidate)
print(res)

