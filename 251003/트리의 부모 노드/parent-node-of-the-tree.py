n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

class Node:
    def __init__(s, num):
        s.num = num
        s.children = []
    
    def add_child(s, node):
        s.children.append(node)

    def __repr__(s):
        return f"({s.num}: {s.children})"

nodes = [Node(i) for i in range(1, n + 1)]
for e1, e2 in edges:
    e1, e2 = e1 - 1, e2 - 1
    nodes[e1].add_child(nodes[e2])

parents = [0] * (n + 1)

# DFS
root = nodes[0]
stk = [root]
while stk:
    node = stk.pop()

    for adj in node.children:
        parents[adj.num] = node.num
        stk.append(adj)

print(*parents[2:], sep='\n')