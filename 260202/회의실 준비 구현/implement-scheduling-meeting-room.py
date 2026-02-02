n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: x[1])

result = []
for m in meetings:
    if not result:
        result.append(m)
        continue
    last = result[-1]
    if last[1] <= m[0]:
        result.append(m)

print(len(result))

