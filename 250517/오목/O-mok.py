n = 19
board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
result = 0
winner_center = (-1, -1)

# 가로 탐색
for i in range(n):
    for j in range(n - 5 + 1):
        if board[i][j] == 0:
            continue

        is_five = True
        for k in range(j, j + 4):
            if board[i][k] != board[i][k + 1]:
                is_five = False
        if is_five:
            result = board[i][j]
            winner_center = (i + 1, j + 3)

# 세로 탐색
for i in range(n):
    for j in range(n - 5 + 1):
        if board[j][i] == 0:
            continue

        is_five = True
        for k in range(j, j + 4):
            if board[k][i] != board[k + 1][i]:
                is_five = False
        if is_five:
            result = board[j][i]
            winner_center = (j + 3, i + 1)

# 우하단 대각선 탐색
for i in range(n - 5 + 1):
    for j in range(n - 5 + 1):
        if board[i][j] == 0:
            continue

        is_five = True
        for k in range(5):
            if board[i][j] != board[i + k][j + k]:
                is_five = False
        if is_five:
            result = board[i][j]
            winner_center = (i + 3, j + 3)

# 좌하단 대각선 탐색
for i in range(n - 5 + 1):
    for j in range(4, n):
        if board[i][j] == 0:
            continue

        is_five = True
        for k in range(5):
            if board[i][j] != board[i + k][j - k]:
                is_five = False
        if is_five:
            result = board[i][j]
            winner_center = (i + 3, j - 2 + 1)

print(result)
print(*winner_center if winner_center != (-1, -1) else '')