n = int(input())
heights = [int(input()) for _ in range(n)]
maxh = max(heights)

res = 0
for h in range(1, maxh):
    iceberg = 0

    for j in range(1, n):
        if heights[j] <= h and heights[j - 1] > h:
            iceberg += 1
    if heights[-1] > h:
        iceberg += 1
    res = max(res, iceberg)

print(res)