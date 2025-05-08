n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
idx = 0
cnt = 0
while idx < n:
    if arr[idx]:
        cnt += 1
        idx += 2 * m + 1
    else:
        idx += 1
print(cnt)