n, k, b = map(int, input().split())
missing = [int(input()) for _ in range(b)]
miss_check = [False] * (n + 1)

for m in missing:
    miss_check[m] = True

arr = list(range(1, n + 1))

count = 10**6
missing_count = 0
for i in range(n - k + 1):
    if i == 0:
        for j in range(k):
            if miss_check[arr[j]]:
                missing_count += 1
    else:
        prv, nxt = arr[i - 1], arr[i + k - 1]
        if miss_check[prv]:
            missing_count -= 1
        if miss_check[nxt]:
            missing_count += 1

    count = min(count, missing_count)

print(count)