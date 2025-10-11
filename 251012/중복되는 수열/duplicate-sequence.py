n = int(input())
sequences = [input() for _ in range(n)]

class Node:
    def __init__(self):
        self.end = False
        self.children = [None for _ in range(10)]

root = Node()

def insert(word):
    node = root
    for ch in word:
        idx = ord(ch) - ord('0')
        if not node.children[idx]:
            node.children[idx] = Node()
        node = node.children[idx]
    node.end = True

def find_node(root, word):
    node = root
    for ch in word:
        idx = ord(ch) - ord('0')
        node = node.children[idx]
    return node

def dfs(start):
    for adj in start.children:
        if adj:
            if adj.end or dfs(adj):
                return True
    return False

for w in sequences:
    insert(w)

res = 1
for w in sequences:
    cur = find_node(root, w)
    if dfs(cur):
        res = 0
print(res)