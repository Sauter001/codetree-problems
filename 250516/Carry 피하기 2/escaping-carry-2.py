n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def check_carry(*nums):
    digit = 10
    tmps = [x for x in nums]
    while any(x % digit != x for x in tmps):
        # print(tmps)
        if sum(x % digit for x in tmps) >= 10:
            return 0
        tmps = [x // digit for x in tmps]
    return sum(nums)

res = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            res = max(res, check_carry(arr[i], arr[j], arr[k]))
            
print(-1 if res == 0 else res)