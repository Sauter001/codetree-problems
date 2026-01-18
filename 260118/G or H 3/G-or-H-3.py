n, k = map(int, input().split())
coordinate = ['X'] * 10001
positions = []
signs = []
for _ in range(n):
    pos, sign = input().split()
    positions.append(int(pos))
    signs.append(sign)

for pos, sign in zip(positions, signs):
    coordinate[pos] = sign

res = 0
for start in range(1, n - (k - 1) + 1):
    snippet = coordinate[start:start + k + 1]
    gs = len(list(filter(lambda x: x == 'G', snippet)))
    hs = 2 * len(list(filter(lambda x: x == 'H', snippet)))
    res = max(res, gs + hs)
print(res)
