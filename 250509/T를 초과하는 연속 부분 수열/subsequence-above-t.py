n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt, res = 0, 0
for i in range(n):
    if (i == 0 and arr[i] > t) or (arr[i - 1] <= t and arr[i] > t):
        cnt = 1
    elif i > 0 and arr[i - 1] > t and arr[i] > t:
        cnt += 1
    else:
        cnt = 0

    res = max(res, cnt)
print(res)