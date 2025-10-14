n, t = map(int, input().split())

ls = list(map(int, input().split()))
rs = list(map(int, input().split()))
ds = list(map(int, input().split()))

def roll(arr):
    val = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = val

for _ in range(t):
    left_end, right_end, down_end = ls[-1], rs[-1], ds[-1]

    roll(ls)
    roll(rs)
    roll(ds)

    ls[0] = down_end
    rs[0] = left_end
    ds[0] = right_end

print(*ls)
print(*rs)
print(*ds)
