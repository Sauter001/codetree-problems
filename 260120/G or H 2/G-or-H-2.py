n = int(input())
MAX_POS = 100
people = [tuple(input().split()) for _ in range(n)]
positions = []
for p in people:
    pos, alpha = p
    pos = int(pos)
    positions.append((pos, 1 if alpha == 'G' else -1))

max_size = 0
POS_INDEX, SIGN_INDEX = 0, 1

# 같은 모양만 있는 곳 판정
start = 0
for i in range(n):
    if i > 0 and positions[i][SIGN_INDEX] != positions[i-1][SIGN_INDEX]:
        start = i
    max_size = max(max_size, positions[i][POS_INDEX] - positions[start][POS_INDEX])

prefix_first = {0: -1}
prefix_sum = 0
for i in range(n):
    prefix_sum += positions[i][SIGN_INDEX]

    if prefix_sum in prefix_first:
        first_idx = prefix_first[prefix_sum]
        if first_idx == -1:
            size = positions[i][POS_INDEX] - positions[0][POS_INDEX]
        else:
            size = positions[i][POS_INDEX] - positions[first_idx + 1][POS_INDEX]
        max_size = max(size, max_size)
    else:
        prefix_first[prefix_sum] = i

print(max_size)