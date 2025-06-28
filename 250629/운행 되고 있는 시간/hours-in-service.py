n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
times.sort()

# Please write your code here.
# print(times)

res = 0
for i in range(n):
    works = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        for t in range(times[j][0], times[j][1]):
            works[t] = 1
    res = max(res, sum(works))
print(res)