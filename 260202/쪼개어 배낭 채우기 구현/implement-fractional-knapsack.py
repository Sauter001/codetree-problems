N, capacity = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
weights, values = list(w), list(v)

unit_prices = sorted(
        [(i, values[i] / weights[i]) for i in range(N)], 
        key=lambda x: x[1], 
        reverse=True)
cur_capacity = capacity
res = 0

for idx, up in unit_prices:
    count = 0
    while count < weights[idx] and cur_capacity > 0:
        cur_capacity -= 1
        res += up
        count += 1

print('%.3f' % (res))


