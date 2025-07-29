N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
bomb_nums = set(nums)

res = -1
for b in bomb_nums:
    for i in range(N):
        if nums[i] == b:
            for j in range(i + 1, min(N, i + K + 1)):
                if nums[i] == nums[j]:
                    res = max(res, nums[i])
print(res)        
