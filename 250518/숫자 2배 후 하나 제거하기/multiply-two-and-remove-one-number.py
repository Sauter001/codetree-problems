from functools import reduce

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min_diff = 10000
for i in range(n):
    doubled_arr = arr[:]
    doubled_arr[i] *= 2
    for j in range(n):
        removed_arr = [x for idx, x in enumerate(doubled_arr) if idx != j]
        diff = sum([abs(removed_arr[k] - removed_arr[k + 1]) for k in range(len(removed_arr) - 1)])
        # print(removed_arr, diff)
        min_diff = min(min_diff, diff)
print(min_diff)
    
