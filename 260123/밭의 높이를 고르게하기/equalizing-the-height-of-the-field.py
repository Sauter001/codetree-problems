n, height, trial = map(int, input().split())
arr = list(map(int, input().split()))
diff_arr = sorted([abs(x - height) for x in arr], reverse=True)

count = 0
trial_count = len(list(filter(lambda d: d == 0, diff_arr)))

while trial_count <= trial:
    trial_count += 1
    if not diff_arr:
        break

    diff = diff_arr.pop()
    if diff != 0:
        count += diff
    
print(count)