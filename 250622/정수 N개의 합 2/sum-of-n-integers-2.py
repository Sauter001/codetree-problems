n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
sums = [0] * (n + 1)
for i in range(n):
    sums[i + 1] = sums[i] + arr[i]

res = -1000
for i in range(n - k + 1):
    if res < sums[i + k] - sums[i]:
        res = sums[i + k] - sums[i]

print(res)