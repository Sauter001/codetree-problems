from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr_counter = Counter(arr)

sorted_entries = sorted(arr_counter.items(), key=lambda x: (-x[1], -x[0]))
print(sorted_entries)