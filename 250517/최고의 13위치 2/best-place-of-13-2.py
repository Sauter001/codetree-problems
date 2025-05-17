n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(n - 3 + 1):
        for k in range(n):
            for l in range(n - 3 + 1):
                if i == k and l < j + 3:
                    continue
                res = max(res, sum(arr[i][j:j+3]) + sum(arr[k][l:l+3]))
print(res)
