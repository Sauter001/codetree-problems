n, m = map(int, input().split())

# Process robot A's movements
t_a = []
d_a = []
for _ in range(n):
    time, direction = input().split()
    t_a.append(int(time))
    d_a.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
pos_a, pos_b = [], []
cur_a = cur_b = 0

for t, d in zip(t_a, d_a):
    direction = -1 if d == 'L' else 1
    for i in range(t):
        cur_a += direction
        pos_a.append(cur_a)

for t, d in zip(t_b, d_b):
    direction = -1 if d == 'L' else 1
    for i in range(t):
        cur_b += direction
        pos_b.append(cur_b)

common_idx = min(len(pos_a), len(pos_b))
count = 0
for i in range(common_idx - 1):
    if pos_a[i] != pos_b[i] and pos_a[i + 1] == pos_b[i + 1]:
        count += 1

pos_to_search = pos_a if common_idx < len(pos_a) else pos_b
pos_shorter = pos_a if common_idx == len(pos_a) else pos_b

for i in range(common_idx, len(pos_to_search) - 1):
    if pos_to_search[i] != pos_shorter[-1] and pos_to_search[i + 1] == pos_shorter[-1]:
        count += 1
print(count)
