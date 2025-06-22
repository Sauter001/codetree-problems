n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
sums = [0] * (n + 1)
for i in range(n):
    sums[i] = sums[i + 1] + arr[i]

print(sums)
