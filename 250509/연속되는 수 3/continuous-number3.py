N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
def sgn(x):
    return -1 if x < 0 else (1 if x > 0 else 0)

cnt, result = 0, 0
for i in range(N):
    if i == 0 or sgn(arr[i]) != sgn(arr[i - 1]):
        cnt = 1
    else: 
        cnt += 1
    result = max(result, cnt)
print(result)