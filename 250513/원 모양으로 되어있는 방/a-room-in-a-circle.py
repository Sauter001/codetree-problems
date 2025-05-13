n = int(input())
people_per_room = [int(input()) for _ in range(n)]

# Please write your code here.
weights = list(range(n))
result = 100 ** 6
for i in range(n):
    candidate = sum(list(map(lambda x, y: x * y, people_per_room, weights)))
    result = min(result, candidate)
    weights.append(weights.pop(0))
print(result)
