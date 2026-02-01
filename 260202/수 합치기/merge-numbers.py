import heapq as hq

n = int(input())
arr = list(map(int, input().split()))

hq.heapify(arr)
res = 0
while len(arr) > 1:
    e1 = hq.heappop(arr)
    e2 = hq.heappop(arr)

    s = e1 + e2
    res += s
    hq.heappush(arr, s)
print(res)