n = int(input())
arr = list(map(int, input().split()))
max_s = arr[0]
s = 0

for x in arr:
    if s + x < 0:
        s = 0
        max_s = max(max_s, s)
        continue
    s += x
    max_s = max(max_s, s)

print(s)
