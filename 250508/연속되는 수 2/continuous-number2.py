n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt, result = 0, 0

for i in range(n):
    if i == 0 or arr[i] != arr[i - 1]:
        cnt = 1
    else:
        cnt += 1
    result = max(cnt, result)

print(result)