n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

shortest_dist = 10000
for skip_point in range(1, n-1):
    path = [(0, 0)]
    for i in range(n):
        if i == skip_point: continue
        path.append((x[i], y[i]))
    
    distance_skipped = 0
    for i in range(len(path) - 1):
        src_x, src_y = path[i]
        dest_x, dest_y = path[i + 1]
        distance_skipped += distance(src_x, src_y, dest_x, dest_y)
    shortest_dist = min(shortest_dist, distance_skipped)
print(shortest_dist)


