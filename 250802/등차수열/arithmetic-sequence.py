n = int(input())
arr = list(map(int, input().split()))

left, right = min(arr), max(arr)

res = 0
for k in range(left + 1, right):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] - k == k - arr[i]:
                count += 1
    res = max(res, count)   

print(res)