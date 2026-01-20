n, k = map(int, input().split())
MAX_POS = 100
coordinate = [0] * (MAX_POS + 1)

for _ in range(n):
    c, p = map(int, input().split())
    coordinate[p] += c

count = 0
for center in range(k, MAX_POS - k + 1):
    min_idx = max(0, center - k)
    max_idx = min(MAX_POS, center + k)
    sliced = coordinate[min_idx:max_idx+1]
    count = max(count, sum(sliced))

print(count)
