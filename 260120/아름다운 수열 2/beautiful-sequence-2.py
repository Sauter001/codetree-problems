import sys
from collections import defaultdict, Counter
input = sys.stdin.readline

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
b_counter = Counter(b_list)
count = 0
for i in range(n - m + 1):
    target = a_list[i:i+m]
    if Counter(target) == b_counter:
        count += 1

print(count)