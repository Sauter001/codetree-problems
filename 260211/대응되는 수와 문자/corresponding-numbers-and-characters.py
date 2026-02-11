n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

str_map = {}
index_map = {}

for i in range(1, n + 1):
    str_map[words[i]] = i
    index_map[i] = words[i]

for q in queries:
    if q.isnumeric():
        val = int(q)
        print(index_map[val])
    else:
        print(str_map[q])