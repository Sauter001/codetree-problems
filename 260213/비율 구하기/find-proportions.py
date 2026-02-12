from sortedcontainers import SortedDict
from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

counter = SortedDict(Counter(words))
print(*[f"{k} {v / n * 100:.4f}" for k, v in counter.items()], sep='\n')
