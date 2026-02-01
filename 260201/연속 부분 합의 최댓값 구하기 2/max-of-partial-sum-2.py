n = int(input())
arr = list(map(int, input().split()))
s = 0

for x in arr:
    if s + x < 0:
        s = 0
        continue
    s += x

if s == 0:
    s = max(arr)

print(s)
