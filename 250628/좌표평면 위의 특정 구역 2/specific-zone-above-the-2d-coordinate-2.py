n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
INF = 50000
areas = []
for i in range(n):
    x1, y1, x2, y2 = INF, INF, 0, 0
    for j in range(n):
        if i == j:
            continue
        x1, x2 = min(x1, points[j][0]), max(x2, points[j][0])
        y1, y2 = min(y1, points[j][1]), max(y2, points[j][1])
    areas.append((x2 - x1) * (y2- y1))
# print(areas)
print(min(areas))