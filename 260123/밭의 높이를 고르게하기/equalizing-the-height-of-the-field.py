n, height, trial = map(int, input().split())
arr = list(map(int, input().split()))
diff_arr = [abs(x - height) for x in arr]
diff_prefix = [0] * (n + 1)

s = 0
for i in range(n):
    s += diff_arr[i]
    diff_prefix[i + 1] = s

min_cost = float('inf')
for i in range(n - trial + 1):
    min_cost = min(min_cost, diff_prefix[i + trial] - diff_prefix[i])

print(min_cost)