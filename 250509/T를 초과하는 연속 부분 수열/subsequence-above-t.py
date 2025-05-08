n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt, res = 0, 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 0
print(res)