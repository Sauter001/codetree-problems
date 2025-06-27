n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def distance(start, end):
    return (start[0] - end[0])**2 + (start[1] - end[1])**2

# Please write your code here.
res = 10 ** 6
for i in range(n):
    for j in range(i + 1, n):
        res = min(res, distance(points[i], points[j]))
print(res)