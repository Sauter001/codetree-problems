n, q = map(int, input().split())
MAX_RANGE = 10**6 + 1
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]
axis = [0] * MAX_RANGE

for p in points:
    axis[p] = 1
pf_sum = [0] * (MAX_RANGE + 1)
for i in range(1, MAX_RANGE ):
    pf_sum[i] = pf_sum[i - 1] + axis[i]

for start, end in ranges:
    print(pf_sum[end] - pf_sum[start - 1])
