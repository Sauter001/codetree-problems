from collections import defaultdict, Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))
diff_map = {}
arr_counter = Counter(arr)

for x in arr_counter.keys():
    if k - x == x:
        diff_map[x] = arr_counter[k] // 2
    else:
        diff_map[x] = arr_counter[k - x]

visit_map = defaultdict(bool)
count = 0
for key, val in diff_map.items():
    if visit_map[key]:
        continue
    count += val
    visit_map[k - key] = True

print(count)