n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sums = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + arr[i-1][j-1]

def get_sum(r1, c1, r2, c2):
    return sums[r2][c2] - sums[r1 - 1][c2] - sums[r2][c1 - 1] + sums[r1 - 1][c1 - 1]

# 모든 직사각형 탐색
max_sum = -1
for r1 in range(1, n + 1):
    for c1 in range(1, n + 1):
        for r2 in range(r1, n + 1):
            for c2 in range(c1, n + 1):
                # print('(%d, %d) ~ (%d, %d): %d'%(r1,c1,r2,c2,get_sum(r1, c1, r2, c2)))
                max_sum = max(max_sum, get_sum(r1, c1, r2, c2))

print(max_sum)