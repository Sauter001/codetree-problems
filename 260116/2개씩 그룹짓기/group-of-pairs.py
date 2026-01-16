n = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = []

while nums:
    min_val = nums.pop(0)
    max_val = nums.pop()
    result.append(min_val + max_val)
    nums.sort()

print(max(result))    



