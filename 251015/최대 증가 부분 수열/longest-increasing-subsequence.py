n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    max_idx, max_val = 0, -1
    for j in range(i):
        if arr[j] < arr[i] and max_val < arr[j]:
            max_idx, max_val = j, arr[j]
    dp[i] = dp[max_idx] + 1

print(max(dp))