n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
for value in coins[::-1]:
    while k - value >= 0:
        k -= value
        count += 1
print(count)