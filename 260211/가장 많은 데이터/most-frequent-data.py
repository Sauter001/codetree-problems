from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]
counter = defaultdict(int)

for w in words:
    counter[w] += 1

print(max(counter.values()))