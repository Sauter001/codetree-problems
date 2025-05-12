R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
result = 0
for i in range(1, R):
    for j in range(1, C):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                path = [grid[0][0], grid[i][j], grid[k][l], grid[-1][-1]]
                # print(f"path = {path}, via ({i},{j}) → ({k},{l})")
                if all(path[x] != path[x + 1] for x in range(len(path) - 1)):
                    result += 1
print(result)
