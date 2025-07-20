N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
min_t, max_t = min([t[0] for t in ranges]), max([t[1] for t in ranges])

def get_amount(ta, tb, target):
    if target < ta:
        return C
    elif target <= tb:
        return G
    else:
        return H

res = 0
for t in range(min_t - 1, max_t + 2):
    temp = 0
    for start, end in ranges:
        temp += get_amount(start, end, t)
    res = max(res, temp)
print(res)


