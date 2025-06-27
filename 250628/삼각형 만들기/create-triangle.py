n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
res = 0

def area_of_triangle(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1]) - (p2[0]*p1[1] + p3[0]*p2[1])


for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            selected_points = [points[i], points[j], points[k]]
            xset = set(p[0] for p in selected_points)
            yset = set(p[1] for p in selected_points)
            if len(xset) == 2 and len(yset) == 2:
                res = max(res, area_of_triangle(*selected_points))


print(res)