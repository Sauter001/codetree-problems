n, k, b = map(int, input().split())
arr = [0] * (n + 1)

for _ in range(b):
    x = int(input())
    arr[x] = 1

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

count = float('inf')
for i in range(n - k + 2):
    count = min(count, prefix_sum[i + k - 1] - prefix_sum[i])
print(count)