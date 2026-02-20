import sys
from collections import deque

input = sys.stdin.readline

n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]
wind_queue = deque()

def shift(row_idx, d):
    def shift_left(row_idx):
        row = arr[row_idx]
        row.append(row.pop(0))
    def shift_right(row_idx):
        row = arr[row_idx]
        row.insert(0, row.pop())
    if d == 'L':
        shift_right(row_idx)
    elif d == 'R':
        shift_left(row_idx)

def in_range(row_idx):
    return 0 <= row_idx < n

def get_counter_dir(d):
    return 'R' if d == 'L' else 'L'

def is_propagatable(r1, r2):
    for j in range(m):
        if arr[r1][j] == arr[r2][j]:
            return True
    return False

for wind in winds:
    row_idx, d = wind
    row_idx -= 1    
    shift(row_idx, d)
    upper, lower = row_idx - 1, row_idx + 1
    
    prev = row_idx
    prev_dir = d
    while upper >= 0:
        if not is_propagatable(prev, upper):
            break
        counter_dir = get_counter_dir(prev_dir)
        shift(upper, counter_dir)
        prev_dir = counter_dir
        prev = upper
        upper -= 1

    prev = row_idx
    prev_dir = d
    while lower < n:
        if not is_propagatable(prev, lower):
            break
        counter_dir = get_counter_dir(prev_dir)
        shift(lower, counter_dir)
        prev_dir = counter_dir
        prev = lower
        lower += 1

for row in arr:
    print(*row)