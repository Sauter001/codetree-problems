X, Y = map(int, input().split())
res = 0

# Please write your code here.
for x in range(X, Y + 1):
    tokens = map(int, list(str(x)))
    res = max(res, sum(tokens))
print(res)
