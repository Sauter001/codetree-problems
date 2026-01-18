n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def get_initial_position(k):
    cur_dir_index = 0

    # 방향 결정
    if k <= n:
        cur_dir_index = 0
    elif n < k <= 2*n:
        cur_dir_index = 1
    elif 2*n < k <= 3*n:
        cur_dir_index = 2
    elif 3*n < k:
        cur_dir_index = 3

    # 위치 결정
    pos_x, pos_y = 0, 0
    if k <= n:
        pos_x = 0
        pos_y = (k - 1) % n
    elif n < k <= 2*n:
        pos_x = (k - 1) % n
        pos_y = n - 1
    elif 2*n < k <= 3*n:
        pos_x = n - 1
        pos_y = n - (k - 1) % n - 1
    elif 3*n < k:
        pos_x = n - (k - 1) % n - 1
        pos_y = 0
    return cur_dir_index, (pos_x, pos_y)

def is_out_of_bound(pos) -> bool:
    x, y = pos[0], pos[1]
    return not (0 <= x < n and 0 <= y < n)

def next_dir_index(idx, delta):
    return (idx + delta) % 4

def move(dir_idx, pos):
    px, py = pos
    if grid[px][py] == '/':
        dir_idx = next_dir_index(dir_idx, 1)
        direction = dirs[dir_idx]
        new_pos = (px + direction[0], py + direction[1])
    elif grid[px][py] == '\\':
        dir_idx = next_dir_index(dir_idx, -1)
        direction = dirs[dir_idx]
        new_pos = (px + direction[0], py + direction[1])
    return dir_idx, new_pos


cur_dir_index, cur_pos = get_initial_position(k)
count = 0
while not is_out_of_bound(cur_pos):
    cur_dir_index, cur_pos = move(cur_dir_index, cur_pos)
    count += 1
print(count + 1)