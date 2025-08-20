n = int(input())
arr = list(map(int, input().split()))
s = 0

for x in arr:
    if s < 0:
        s = 0
    s += x
print(s)
