n, k = map(int, input().split())
arr = list(map(int, input().split()))
diff_dict = {}
res = 0
for i in range(n):
    for j in range(i + 1, n):
        diff = k - arr[i] - arr[j]
        if diff in diff_dict:
            res += diff_dict[diff]

    if arr[i] in diff_dict:
        diff_dict[arr[i]] += 1
    else:
        diff_dict[arr[i]] = 1

print(res)