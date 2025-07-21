k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

prior_map = {}

# 전처리
for i in range(1, n + 1):
    prior_map[i] = {x for x in range(1, n + 1)}

for i in range(k):
    for j in range(n):
        rank_set = { arr[i][m] for m in range(j + 1, n) }
        prior_map[arr[i][j]] &= rank_set

res = sum(len(m) for m in prior_map.values())
print(res)