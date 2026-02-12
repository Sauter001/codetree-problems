from collections import defaultdict, Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))
diff_map = {}
arr_counter = Counter(arr)

def combi(x):
    return x(x-1)//2

for x in arr_counter.keys():
    if k - x == x:
        diff_map[x] = combi(arr_counter[x])
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