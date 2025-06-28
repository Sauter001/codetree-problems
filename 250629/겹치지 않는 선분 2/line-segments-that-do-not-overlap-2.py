n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
checks = [False] * n

# Please write your code here.
non_intersect_lines = 0
def is_intersect(line1, line2):
    return (line1[0] < line2[0]) and (line1[1] > line2[1])

for i in range(n):
    result = True
    if checks[i]:
        continue
    for j in range(i + 1, n):
        if is_intersect(lines[i], lines[j]):
            checks[i] = checks[j] = True
            result = False
    non_intersect_lines += 1 if result else 0
print(non_intersect_lines)
