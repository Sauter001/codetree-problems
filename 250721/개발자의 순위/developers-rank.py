k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

prior_map = {}

# 전처리
for i in range(1, n + 1):
    prior_map[i] = {range(1, n + 1)}

for i in range(k):
    for j in range(n):
        rank_set = { arr[i][m] for m in range(j + 1, n) }
        print(rank_set, i)
        prior_map[j + 1] &= rank_set

print(prior_map)


