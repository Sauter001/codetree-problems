n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

shortest_dist = 100 ** 6

total = 0
for i in range(n - 1):
    total += distance(*points[i], *points[i + 1])

for skip_point in range(1, n-1):
    a = distance(*points[skip_point - 1], *points[skip_point])
    b = distance(*points[skip_point], *points[skip_point + 1])
    c = distance(*points[skip_point - 1], *points[skip_point + 1])
    candidate = total - (a + b) + c
    shortest_dist = min(shortest_dist, candidate)
print(shortest_dist)


