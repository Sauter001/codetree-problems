n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def check_carry(*nums):
    tmps = [x for x in nums]
    while any(x > 0 for x in tmps):
        digits = [x % 10 for x in tmps]
        if sum(digits) >= 10:
            return 0
        tmps = [x // 10 for x in tmps]
    return sum(nums)

res = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            res = max(res, check_carry(arr[i], arr[j], arr[k]))
            
print(-1 if res == 0 else res)