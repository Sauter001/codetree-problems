n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dr, dc = [-1, -1, 1, 1], [1, -1, -1, 1]
result = 0

def out_of_bound(r, c):
    return not (0 <= r < n and 0 <= c < n)

def count_rect_from(row, col):
    global result
    for side1 in range(1, n - 1):
        for side2 in range(1, n - 1):
            r1, c1 = row + dr[0]*side1, col + dc[0]*side1  # 1번 방향 끝
            r2, c2 = r1 + dr[1]*side2, c1 + dc[1]*side2 # 2번 방향 끝 (꼭대기)
            r3, c3 = r2 + dr[2]*side1, c2 + dc[2]*side1  # 3번 방향 끝

            # 경계 체크
            if out_of_bound(r1, c1) or out_of_bound(r2, c2) or out_of_bound(r3, c3):
                continue

            total = 0
            cur_row, cur_col = row, col
            for direction in range(4):
                side = side1 if direction % 2 == 0 else side2
                for _ in range(side):
                    total += grid[cur_row][cur_col]
                    cur_row += dr[direction]
                    cur_col += dc[direction]
            result = max(result, total)


for i in range(n):  # 시작행
    for j in range(n): # 시작열
        count_rect_from(i, j)

print(result)