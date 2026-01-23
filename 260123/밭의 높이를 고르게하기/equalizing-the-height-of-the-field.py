n, height, trial = map(int, input().split())
arr = list(map(int, input().split()))
diff_arr = sorted([abs(x - height) for x in arr], reverse=True)
diff_prefix = [0] * (n + 1)

s = 0
for i in range(n):
    s += diff_arr[i]
    diff_prefix[i + 1] = s

# print(diff_prefix)
min_cost = float('inf')
for i in range(n - trial + 1):
    min_cost = min(min_cost, diff_prefix[i + trial - 1] - diff_prefix[i])

print(min_cost)