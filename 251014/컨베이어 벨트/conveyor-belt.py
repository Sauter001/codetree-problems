n, t = map(int, input().split())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))

def roll(arr):
    val = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = val

for i in range(t):
    upper_start, upper_end = upper[0], upper[-1]
    lower_start, lower_end = lower[0], lower[-1]

    roll(upper)
    roll(lower)
    upper[0] = lower_end
    lower[0] = upper_end

print(*upper)
print(*lower)