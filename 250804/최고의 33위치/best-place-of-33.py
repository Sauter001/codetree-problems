n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
mask = [[1] * 3 for _ in range(3)]

res = 0
for i in range(n - 2):
    for j in range(n - 2):
        count = 0
        for k in range(3):
            for l in range(3):
                if grid[i + k][j + l] == 1:
                    count += 1
        res = max(count, res)

print(res)