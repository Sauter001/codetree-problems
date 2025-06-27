n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
res = 0

def area_of_triangle(p1, p2, p3):
    # 신발끈 공식
    return abs((p1[0]*p2[1] + p2[0]*p3[1]) - (p2[0]*p1[1] + p3[0]*p2[1]))

def is_parallel(selected_points):
    x_parallel = y_parallel = False
    for i in range(3):
        for j in range(i + 1, 3):
            # x축에 평행한지
            if selected_points[i][1] == selected_points[j][1]:
                x_parallel = True
            elif selected_points[i][0] == selected_points[j][0]:
                y_parallel = True
    return x_parallel and y_parallel


for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            selected_points = [points[i], points[j], points[k]]
            if is_parallel(selected_points):
                res = max(res, area_of_triangle(*selected_points))

print(res)