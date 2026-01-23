n, height, trial = map(int, input().split())
arr = list(map(int, input().split()))
diff_arr = sorted([abs(x - height) for x in arr], reverse=True)

count = 0
for i in range(trial):
    if not diff_arr:
        break

    diff = diff_arr.pop()
    if diff != 0:
        count += diff

print(count)