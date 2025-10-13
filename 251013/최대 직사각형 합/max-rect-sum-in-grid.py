n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sums = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + arr[i-1][j-1]

def get_sum(r1, c1, r2, c2):
    return sums[r2][c2] - sums[r1 - 1][c2] - sums[r2][c1 - 1] + sums[r1 - 1][c1 - 1]

def find_max_subsum(arr):
    arr_len = len(arr)
    prefix_sum = [0] * arr_len
    for i in range(1, arr_len):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
    res = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            res = max(res, prefix_sum[j] - prefix_sum[i])
    return res

res = -1
for i in range(1, n + 1):
    for j in range(i, n + 1):
        col_sum = [0] * (n + 1)
        for c in range(1, n + 1):
            col_sum[c] = get_sum(i, c, j, c)
            res = max(res, find_max_subsum(col_sum))

print(res)