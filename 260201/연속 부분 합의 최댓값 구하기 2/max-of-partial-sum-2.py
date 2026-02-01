n = int(input())
arr = list(map(int, input().split()))
max_s = arr[0]
s = 0

for x in arr:
    s += x
    max_s = max(max_s, s)
    if s < 0:
        s = 0

print(max_s)
