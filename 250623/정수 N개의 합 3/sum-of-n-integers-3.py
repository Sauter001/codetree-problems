n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
sum_matrix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] \
        - sum_matrix[i-1][j-1] + arr[i - 1][j - 1]

res = 0
print(*sum_matrix, sep='\n')
for i in range(1, n - k + 1):
    for j in range(1, n - k + 1):
        start, end = (i, j), (i + k - 1, j + k - 1)
        candidate = sum_matrix[end[0]][end[1]] \
                    - sum_matrix[start[0] - 1][end[1]] \
                    - sum_matrix[end[0]][start[1] - 1] \
                    + sum_matrix[start[0] - 1][start[1] - 1]
        res = max(res, candidate)

print(res)