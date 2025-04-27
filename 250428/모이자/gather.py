n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
from functools import reduce

max_distance = float('inf')
for i in range(n):
    s = 0
    for j in range(n):
        s += A[j] * abs(i - j)
    max_distance = min(max_distance, s)
print(max_distance)
