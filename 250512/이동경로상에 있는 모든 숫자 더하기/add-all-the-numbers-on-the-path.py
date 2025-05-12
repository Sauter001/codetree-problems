N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Please write your code here.
def movable(r, c):
    return 0 <= r < N and 0 <= c < N

r = c = N // 2 
d = 0
summation = board[r][c]
for cmd in commands:
    match cmd:
        case 'L':
            d = (d - 1) % 4
        case 'R':
            d = (d + 1) % 4
        case 'F':
            nr, nc = r + directions[d][0], c + directions[d][1]
            if movable(nr, nc):
                r, c = nr, nc
                summation += board[r][c]
            
print(summation)