N, M = map(int, input().split())

# Process A's movements
va = []
for _ in range(N):
    vi, ti = map(int, input().split())
    va.append((vi, ti))

# Process B's movements
vb = []
for _ in range(M):
    vi, ti = map(int, input().split())
    vb.append((vi, ti))

# Please write your code here.
pos_a, pos_b = [0], [0]

def record_pos(vs, pos):
    cur = 0
    for v, t in vs:
        for i in range(t):
            pos.append(pos[cur] + v)
            cur += 1   
    
record_pos(va, pos_a)
record_pos(vb, pos_b)

hofs = [] # 0: A, 1: B, 2: A,B
for i in range(len(pos_a[1:])):
    if pos_a[i] > pos_b[i]:
        hofs.append(0)
    elif pos_a[i] < pos_b[i]:
        hofs.append(1)
    else:
        hofs.append(2)

hof_count = 0
for i in range(1, len(hofs)):
    if hofs[i - 1] != hofs[i]:
        hof_count += 1
print(hof_count)
