N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
infected_list = [False] * (N + 1)
infected_list[P] = True
handshake_counts = {dev: 0 for dev in range(N + 1)}
handshakes.sort()

# 감염시키는 사람은 전염됐다고 가정
def infect_person(from_dev, to_dev):
    if handshake_counts[from_dev] < K:
        infected_list[to_dev] = True
    handshake_counts[from_dev] += 1     
    handshake_counts[to_dev] += 1  

for t, x, y in handshakes:
    # print(t,x,y)
    
    if not (infected_list[x] or infected_list[y]):
        continue
    
    if infected_list[x]:
        infect_person(x, y)
    elif infected_list[y]:
        infect_person(y, x)

print(''.join('1' if infected else '0' for infected in infected_list[1:]))