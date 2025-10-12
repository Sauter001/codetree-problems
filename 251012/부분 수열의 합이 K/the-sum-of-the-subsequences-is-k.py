n, k = map(int, input().split())
arr = list(map(int, input().split()))
sums = [0]
acc = 0
for x in arr:
    acc += x
    sums.append(acc)

cnt = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        if sums[j] - sums[i] == k:
            cnt += 1
print(cnt)