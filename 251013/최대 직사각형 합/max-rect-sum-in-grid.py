n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sums = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + arr[i-1][j-1]

def get_sum(r1, c1, r2, c2):
    return sums[r2][c2] - sums[r1 - 1][c2] - sums[r2][c1 - 1] + sums[r1 - 1][c1 - 1]

res = -float('inf')
for i in range(1, n + 1):
    for j in range(i, n + 1):
        cur_sum = 0
        max_per_slice = -float('inf')
        for c in range(1, n + 1):
            cur_col_sum = get_sum(i, c, j, c)
            cur_sum = max(cur_col_sum, cur_sum + cur_col_sum)
            max_per_slice = max(max_per_slice, cur_sum)
        res = max(res, max_per_slice)

print(res)