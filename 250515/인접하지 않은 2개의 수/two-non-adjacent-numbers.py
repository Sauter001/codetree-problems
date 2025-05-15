n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
res = 0
for i in range(n):
    for j in range(i + 2, n):
        res = max(res, numbers[i] + numbers[j])
print(res)