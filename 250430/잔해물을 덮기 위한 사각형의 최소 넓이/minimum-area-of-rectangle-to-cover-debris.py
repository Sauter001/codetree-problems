import sys
input = sys.stdin.readline

x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
width, height = 0, 0
if (x1[0] < x1[1] < x2[0]) or (x1[0] < x2[1] < x2[0]):
    if (y1[0] < y2[1] < y2[0]) or (y1[0] < y1[1] < y2[0]):
        width = x2[0] - x1[0]
        height = y2[0] - y1[0]
    elif (y1[1] <= y1[0] <= y2[1]) and (y1[1] <= y2[0] <= y2[1]):
        width = (x1[1] - x1[0]) if (x1[0] < x1[1] < x2[0]) else (x2[0] - x2[1])
        height = y2[0] - y1[0]
elif (x1[1] <= x1[0] <= x2[1]) and (x1[1] <= x2[0] <= x2[1]):
    width = x2[0] - x1[0]
    if (y1[0] < y1[1] < y2[0]) :
        height = (y1[1] - y1[0]) 
    elif (y1[0] < y2[1] < y2[0]):
        height = (y2[0] - y2[1])
elif (x2[1] <= x1[0]) or (x2[0] <= x1[1]) or (y2[1] <= y1[0]) or (y2[0] <= y1[1]):
        width = x2[0] - x1[0]
        height = y2[0] - y1[0]

print(width * height)
