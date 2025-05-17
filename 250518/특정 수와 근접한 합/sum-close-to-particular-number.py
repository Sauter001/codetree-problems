N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
diff = 10000
for i in range(N):
    for j in range(i + 1, N):
        candidates = [x for idx, x in enumerate(arr) if idx not in (i, j)]
        diff = min(diff, abs(sum(candidates) - S))
print(diff)
