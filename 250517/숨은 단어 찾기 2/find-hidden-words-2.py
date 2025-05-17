N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
target = 'LEE'
first = target[0]
cnt = 0

directions = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1),           (0, 1), 
              (1, -1),  (1, 0),  (1, 1)]

def movable(i, j):
    return 0 <= i < N and 0 <= j < M
    
def count_target(i, j, dr, dc):
    for cur in range(1, len(target)):
        nr, nc = i + cur * dr, j + cur * dc
        if not movable(nr, nc) or arr[nr][nc] != target[cur]:
            return 0
            
    return 1
        

for i in range(N):
    for j in range(M):
        if arr[i][j] == first:
            for dr, dc in directions:
                cnt += count_target(i, j, dr, dc)

print(cnt)
