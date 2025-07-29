from itertools import combinations

n = int(input())
axis = [0] * 120
lines = []

for _ in range(n):
    left, right = map(int, input().split())
    for i in range(left, right + 1):
        axis[i] += 1
    lines.append((left, right))

count = 0
for candidates in combinations(lines, 3):
    tmp_axis = axis[:]

    for li in candidates:
        left, right = li
        for i in range(left, right + 1):
            tmp_axis[i] -= 1
    
    if all(x < 2 for x in tmp_axis):
        count += 1
print(count)